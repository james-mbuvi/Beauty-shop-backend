from flask_bcrypt import Bcrypt
from app import app
from models import db, Employee, Review, Leave
from sqlalchemy import text

bcrypt = Bcrypt(app)

from app import db, Category

def seed_data():
    categories = ['Skincare', 'Makeup', 'Scents']
    for category_name in categories:
        category = Category(name=category_name)
        db.session.add(category)
    db.session.commit()

if __name__ == '__main__':
    seed_data()
