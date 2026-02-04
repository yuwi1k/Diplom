const API_URL = "http://127.0.0.1:5000/api";

let myChart = null;
let currentPage = 1;
let totalReviews = 0;
let loadedReviews = 0;


async function updateStats() {
    const res = await fetch(`${API_URL}/stats`);
    const data = await res.json();

    document.getElementById("totalCount").textContent =
        `Всего отзывов: ${data.total}`;

    const ctx = document.getElementById("sentimentChart").getContext("2d");
    if (myChart) myChart.destroy();

    myChart = new Chart(ctx, {
    type: "doughnut",
    data: {
        labels: ["Позитив", "Нейтрально", "Негатив"],
        datasets: [{
            data: data.distribution,
            backgroundColor: [
                "#4CAF50", // Позитив (зелёный)
                "#FFC107", // Нейтрально (жёлтый)
                "#F44336"  // Негатив (красный)
            ]
        }]
    }
});
}


async function loadReviews(reset = false) {

    if (reset) {
        currentPage = 1;
        loadedReviews = 0;
        document.getElementById("reviewsList").innerHTML = "";
    }

    const res = await fetch(`${API_URL}/reviews?page=${currentPage}`);
    const data = await res.json();

    totalReviews = data.total;

    const list = document.getElementById("reviewsList");

    data.reviews.forEach(r => {
        list.innerHTML += `
            <div class="review-item ${r.sentiment}">
                <strong>[${r.source}]</strong> ${r.text}<br>
                <small>Тональность: ${r.sentiment}
                (${Math.round(r.score * 100)}%)</small>
            </div>
        `;
    });

    loadedReviews += data.reviews.length;

    if (loadedReviews >= totalReviews) {
        document.getElementById("loadMoreBtn").style.display = "none";
    } else {
        document.getElementById("loadMoreBtn").style.display = "block";
    }
}


function loadMoreReviews() {
    currentPage += 1;
    loadReviews();
}


async function analyzeText() {
    const text = document.getElementById("inputText").value;
    if (!text) return;

    await fetch(`${API_URL}/analyze`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ text })
    });

    document.getElementById("inputText").value = "";
    refreshAll();
}


async function generateReview() {
    await fetch(`${API_URL}/generate`);
    refreshAll();
}


function refreshAll() {
    updateStats();
    loadReviews(true);
}

refreshAll();


// --- FIX: делаем функции доступными для кнопок ---
window.generateReview = generateReview;
window.analyzeText = analyzeText;
window.loadMoreReviews = loadMoreReviews;
