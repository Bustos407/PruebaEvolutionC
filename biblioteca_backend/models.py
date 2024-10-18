from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Autor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    libros = db.relationship('Libro', backref='autor', lazy=True)

class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor_id = db.Column(db.Integer, db.ForeignKey('autor.id'), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    cantidad_disponible = db.Column(db.Integer, nullable=False)
