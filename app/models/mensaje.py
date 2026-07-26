from app import db
from datetime import datetime

class MensajeContacto(db.Model):
    __tablename__ = 'mensajes_contacto'

    id      = db.Column(db.Integer, primary_key=True)
    nombre  = db.Column(db.String(120), nullable=False)
    email   = db.Column(db.String(120), nullable=False)
    asunto  = db.Column(db.String(200))
    mensaje = db.Column(db.Text, nullable=False)
    fecha   = db.Column(db.DateTime, default=datetime.utcnow)
    leido   = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<MensajeContacto {self.nombre} - {self.email}>'