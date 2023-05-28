from ..service.student_service import setStudent, getStudents

def saveStudent(form):
    dataDict = {
            'document_number': form['document_number'],
            'first_name': form['first_name'],
            'second_name': form['second_name'],
            'lastname': form['lastname'],
            'email': form['email'],
            'birth_date': form['birth_date'],
        }
    return setStudent(data=dataDict)

def listStudent():
    return getStudents()