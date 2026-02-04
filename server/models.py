from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    source = db.Column(db.String(50), nullable=False)
    text = db.Column(db.Text, nullable=False)

    sentiment = db.Column(db.String(20), nullable=False)
    score = db.Column(db.Float, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "source": self.source,
            "text": self.text,
            "sentiment": self.sentiment,
            "score": self.score,
            "created_at": self.created_at.isoformat()
        }
