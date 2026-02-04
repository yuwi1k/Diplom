import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # SQLite база данных
    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///" + os.path.join(basedir, "reviews.db")
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
