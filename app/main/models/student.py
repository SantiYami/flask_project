from ...extensions import db
from datetime import datetime, date
from sqlalchemy.orm.collections import attribute_mapped_collection
from sqlalchemy.ext.hybrid import hybrid_property

class Student(db.Model):
    __tablename__ = 'estudiante'
    
    def dateNow(self):
        return datetime.now()
    
    id_student = db.Column('id_estudiante', db.Integer, db.Identity(), primary_key=True, key='id_student', info={'column':'id_estudiante'})
    document_number = db.Column('no_documento', db.String(30), nullable=False, key='document_number', info={'column':'no_documento'})
    first_name = db.Column('primer_nombre', db.String(100), nullable=False, key='first_name', info={'column':'primer_nombre'})
    second_name = db.Column('segundo_nombre', db.String(100), nullable=True, key='second_name', info={'column':'segundo_nombre'})
    lastname = db.Column('apellido', db.String(100), nullable=False, key='lastname', info={'column':'apellido'})
    email = db.Column('correo', db.String(150), nullable=False, key='email', info={'column':'correo'})
    birth_date = db.Column('fecha_nacimiento', db.Date, nullable=False, key='birth_date', info={'column':'fecha_nacimiento'})
    creation_date = db.Column('fecha_creo', db.DateTime, nullable=False, comment='fecha en que se creo el registro en el sistema', default=dateNow, server_default=db.func.now())
    
    course = db.relationship('StudentCourse', backref='student', lazy=True)
    
    @hybrid_property
    def nameComplete(self):
        return f'{self.first_name} {self.second_name if self.second_name != None else ""} {self.lastname}'
    
    @hybrid_property
    def age(self):
        today = date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
    
    @hybrid_property
    def average(self):
        notes = [ec.note for ec in self.course if ec.note is not None]
        if notes:
            return sum(notes) / len(notes)
        else:
            return None

    @hybrid_property
    def programName(self):
        return self.course[0].course.program.name if self.course else None
    
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id_student': self.id_student,
            'document_number': self.document_number,
            'nameComplete': self.nameComplete,
            'first_name': self.first_name,
            'second_name': self.second_name,
            'lastname': self.lastname,
            'email': self.email,
            'average': self.average,
            'programName': self.programName,
            'birth_date': self.birth_date,
            'age': self.age,
        }