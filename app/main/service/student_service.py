import logging

from ...extensions import db
from ..models.student import Student
from ..models.program import Program
from ..models.course import Course
from ..models.student_course import StudentCourse

def setStudent(data):
    try:
        newStudent = Student(
            document_number = data.get("document_number"),
            first_name = data.get("first_name"),
            second_name = data.get("second_name"),
            lastname = data.get("lastname"),
            email = data.get("email"),
            birth_date = data.get("birth_date")
        )
        
        db.session.add(newStudent)
        db.session.flush()
        
        db.session.commit()
        
        response = {
            "message": "Estudiante guardado",
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

def getStudents():
    try:
        data = Student.query.all()
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