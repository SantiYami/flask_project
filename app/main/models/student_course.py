from ...extensions import db
from datetime import datetime

class StudentCourse(db.Model):
    __tablename__ = 'estudiante_curso'
    
    def dateNow(self):
        return datetime.now()
    
    id_student = db.Column('id_estudiante', db.Integer, db.ForeignKey('estudiante.id_student'), primary_key=True, key='id_student', info={'column':'id_estudiante'})
    id_course = db.Column('id_curso', db.Integer, db.ForeignKey('curso.id_course'), primary_key=True, key='id_course', info={'column':'id_curso'})
    note = db.Column('nota', db.Numeric(3,2), nullable=True, key='note', info={'column':'nota'})
    creation_date = db.Column('fecha_creo', db.DateTime, nullable=False, comment='fecha en que se creo el registro en el sistema', default=dateNow, server_default=db.func.now())