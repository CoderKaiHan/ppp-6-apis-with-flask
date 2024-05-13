from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Reptile(db.Model):
    __tablename__ = "reptiles"

    id = db.Column(db.Integer, primary_key=True)
    common_name = db.Column(db.String(250), nullable=False, unique=False)
    scientificf_name = db.Column(db.String(250), nullable=False, unique=False)
    conservation_status = db.Column(db.String(250), nullable=False)
    native_habitat = db.Column(db.String(250), nullable=False)
    fun_facts = db.Column(db.Text, nullable=True)
