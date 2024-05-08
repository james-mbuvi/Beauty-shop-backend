from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates, relationship
from sqlalchemy.ext.associationproxy import association_proxy
import re

db = SQLAlchemy()

#define models
class User(db.Model):
    pass


class Category(db.Model):
    pass





class Product(db.Model):
    pass






    