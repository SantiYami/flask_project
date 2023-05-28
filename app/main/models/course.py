from ...extensions import db
from datetime import datetime

class Course(db.Model):
    __tablename__ = 'curso'
    
    def dateNow(self):
        return datetime.now()
    
    id_course = db.Column('id_curso', db.Integer, db.Identity(), primary_key=True, key='id_course', info={'column':'id_curso'})
    name = db.Column('nombre', db.String(100), nullable=False, key='name', info={'column':'nombre'})
    description = db.Column('descripcion', db.String(500), nullable=True, key='description', info={'column':'descripcion'})
    id_program = db.Column('id_programa', db.Integer, db.ForeignKey('programa.id_program'), nullable=False, key='id_program', info={'column':'id_programa'})
    creation_date = db.Column('fecha_creo', db.DateTime, nullable=False, comment='fecha en que se creo el registro en el sistema', default=dateNow, server_default=db.func.now())

    students = db.relationship('StudentCourse', backref='course', lazy=True)
