from sqlalchemy import delete

from app import app
from models import db, User


def seed():
    """Seed tables"""
    db.session.execute(delete(User))
    user1 = User(name="user1", password="secret")
    db.session.add(user1)
    user2 = User(name="user2", password="secret", email = "user@@company.co")
    db.session.add(user2)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        seed()
