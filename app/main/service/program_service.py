import logging

from ...extensions import db
from ..models.student import Student
from ..models.program import Program
from ..models.course import Course
from ..models.student_course import StudentCourse

def setProgram(data):
    try:
        newProgram = Program(
            name = data.get("name"),
            description = data.get("description"),
        )
        
        db.session.add(newProgram)
        db.session.flush()
        
        db.session.commit()
        
        response = {
            "message": "Programa guardado",
        }
        return response, 200
    except Exception as e:
        logging.error(e)
        db.session.rollback()
        response = {
            "message": "Error: " + str(e),
        }
        return response, 500
    finally:
        db.session.close()

def getPrograms():
    try:
        data = Program.query.all()
        response = [item.serialize for item in data]
        return response, 200
    except Exception as e:
        logging.error(e)
        response = {
            "message": "Error: " + str(e),
        }
        return response, 500
    finally:
        db.session.close()