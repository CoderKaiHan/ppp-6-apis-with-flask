from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Reptile(db.Model):
    __tablename__ = "reptiles"

    id = db.Column(db.Intger, primary_key=True)
    reptile_name = db.Column(db.String(250), nullable=False, unique=True)
    information = db.Column(db.Text, nullable=False)
    submitter = db.Column(db.String(250), nullable=True)
