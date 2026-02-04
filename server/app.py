from flask import Flask, jsonify, request
from flask_cors import CORS
import os

from config import Config
from models import db, Review

from services.nlp_service import analyzer
from services.generator import generate_fake_review


# -------------------------------
# Настройка путей проекта
# -------------------------------

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

app = Flask(
    __name__,
    static_folder=os.path.join(BASE_DIR, "client"),
    static_url_path=""
)

CORS(app)

# -------------------------------
# Подключение конфигурации БД
# -------------------------------

app.config.from_object(Config)
db.init_app(app)


# -------------------------------
# Главная страница (index.html)
# -------------------------------

@app.route("/")
def home():
    """
    Открывает клиентский интерфейс
    http://127.0.0.1:5000/
    """
    return app.send_static_file("index.html")


# -------------------------------
# API: анализ вручную
# -------------------------------

@app.route("/api/analyze", methods=["POST"])
def analyze_manual():
    data = request.json
    text = data.get("text", "")

    sentiment, score = analyzer.analyze(text)

    new_review = Review(
        source="manual",
        text=text,
        sentiment=sentiment,
        score=score
    )

    db.session.add(new_review)
    db.session.commit()

    return jsonify(new_review.to_dict())


# -------------------------------
# API: генерация отзыва
# -------------------------------

@app.route("/api/generate", methods=["GET"])
def generate_review():
    text, source = generate_fake_review()
    sentiment, score = analyzer.analyze(text)

    new_review = Review(
        source=source,
        text=text,
        sentiment=sentiment,
        score=score
    )

    db.session.add(new_review)
    db.session.commit()

    return jsonify(new_review.to_dict())


# -------------------------------
# API: статистика
# -------------------------------

@app.route("/api/stats", methods=["GET"])
def get_stats():
    total = Review.query.count()

    positive = Review.query.filter_by(sentiment="positive").count()
    neutral = Review.query.filter_by(sentiment="neutral").count()
    negative = Review.query.filter_by(sentiment="negative").count()

    return jsonify({
        "total": total,
        "distribution": [positive, neutral, negative]
    })


# -------------------------------
# API: отзывы (пагинация)
# -------------------------------

@app.route("/api/reviews", methods=["GET"])
def get_reviews():
    """
    Пример:
    /api/reviews?page=1
    /api/reviews?page=2
    """

    page = int(request.args.get("page", 1))
    per_page = 10

    query = Review.query.order_by(Review.created_at.desc())

    total = query.count()

    reviews = query.offset((page - 1) * per_page).limit(per_page).all()

    return jsonify({
        "total": total,
        "page": page,
        "reviews": [r.to_dict() for r in reviews]
    })


# -------------------------------
# Запуск сервера
# -------------------------------

if __name__ == "__main__":
    app.run(debug=True, port=5000)
