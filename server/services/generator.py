import random

SOURCES = ['vk', 'telegram', 'ozon', 'wildberries']

REVIEWS = {
    "positive": [
        "Отличный товар, качество реально порадовало.",
        "Очень доволен покупкой, рекомендую друзьям.",
        "Быстрая доставка, всё пришло идеально.",
        "Сервис на высоте, буду заказывать ещё."
    ],
    "negative": [
        "Ужасное обслуживание, больше не обращусь.",
        "Товар приехал сломанным, разочарование.",
        "Не стоит своих денег вообще.",
        "Верните деньги, это просто кошмар."
    ],
    "neutral": [
        "Ну такое, обычный товар без вау-эффекта.",
        "Ничего особенного, ожидал большего.",
        "В целом нормально, но есть минусы.",
        "Средний опыт, не плохо и не отлично."
    ]
}


def generate_fake_review():
    sentiment_type = random.choice(list(REVIEWS.keys()))
    text = random.choice(REVIEWS[sentiment_type])
    source = random.choice(SOURCES)

    return text, source
