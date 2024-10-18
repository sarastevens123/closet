# MODEL FOR SQLALCHEMY TABLES


from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declaritive_base 
from sqlalchemy.orm import sessionmaker

db = create_engine()
database_url = 'postgresql://username:password@host/closet_db'

class Sock(db.model):

    __tablename__ = "socks"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    color = db.Column(db.String(50), nullable=False)
    purchase_year = db.Column(db.Integer)
    brand = db.Column(db.String(50))
    value = db.Column(db.Integer)

    def __repr__(self):
        return f"<This is a {self.size}, {self.color} sock"


class Shoe(db.model):

    __tablename__ = "shoes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    color = db.Column(db.String(50), nullable=False)
    size = db.Column(db.Float, nullable=False)
    purchase_year = db.Column(db.Integer)
    brand = db.Column(db.String(50),nullable=False)
    value = db.Column(db.Integer)

    def __repr__(self):
        return f"<This is a {self.color}, {self.brand} shoe"
    
class Jacket(db.model):

    __tablename__ = "jackets"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    color = db.Column(db.String(50), nullable=False)
    size = db.Column(db.String(20), nullable=False)
    purchase_year = db.Column(db.Integer)
    brand = db.Column(db.String(50), nullable=False)
    value = db.Column(db.Integer)
    type = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<This is a {self.color}, {self.brand} {self.type} jacket"
    
class Pant(db.model):

    __tablename__ = "pants"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    color = db.Column(db.String(50), nullable=False)
    size = db.Column(db.String(20), nullable=False)
    purchase_year = db.Column(db.Integer)
    brand = db.Column(db.String(50), nullable=False)
    value = db.Column(db.Integer)
    type = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<This is a {self.color}, {self.brand} {self.type} pant"
    
class Shirt(db.model):

    __tablename__ = "shirts"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    color = db.Column(db.String(50), nullable=False)
    size = db.Column(db.String(20), nullable=False)
    purchase_year = db.Column(db.Integer)
    brand = db.Column(db.String(50), nullable=False)
    value = db.Column(db.Integer)
    type = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<This is a {self.color}, {self.brand} {self.type} shirt"
    

def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///closet_db"
    app.config["SQLALCHEMY_ECHO"] = False
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    print("Connected to db!")



if __name__ == "__main__":
    from flask import Flask

    app = Flask(__name__)
    connect_to_db(app)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= True
    

