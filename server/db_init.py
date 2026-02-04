from flask import Flask
from config import Config
from models import db


def init_database():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()
        print("✅ Таблицы созданы успешно")


if __name__ == "__main__":
    init_database()
