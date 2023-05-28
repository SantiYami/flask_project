from ...extensions import db
from datetime import datetime

class Program(db.Model):
    __tablename__ = 'programa'
    
    def dateNow(self):
        return datetime.now()
    
    id_program = db.Column('id_programa', db.Integer, db.Identity(), primary_key=True, key='id_program', info={'column':'id_programa'})
    name = db.Column('nombre', db.String(100), nullable=False, key='name', info={'column':'nombre'})
    description = db.Column('descripcion', db.String(500), nullable=True, key='description', info={'column':'descripcion'})
    creation_date = db.Column('fecha_creo', db.DateTime, nullable=False, comment='fecha en que se creo el registro en el sistema', default=dateNow, server_default=db.func.now())
    
    courses = db.relationship('Course', backref='program', lazy=True)
    
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id_program': self.id_program,
            'name': self.name,
            'description': self.description,
        }