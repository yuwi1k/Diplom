from transformers import pipeline


class SentimentAnalyzer:
    def __init__(self):
        self.model = pipeline(
            "sentiment-analysis",
            model="cointegrated/rubert-tiny-sentiment-balanced"
        )

    def analyze(self, text: str):
        if not text.strip():
            return "neutral", 0.0

        result = self.model(text[:512])[0]

        label = result["label"].lower()
        score = float(result["score"])

        # правильная нормализация
        if "pos" in label:
            return "positive", round(score, 3)

        if "neg" in label:
            return "negative", round(score, 3)

        return "neutral", round(score, 3)


analyzer = SentimentAnalyzer()
