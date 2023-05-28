from flask import render_template, request
from app.main.blueprint.students import bp

from ...controller.student_controller import saveStudent, listStudent

# * /students/

@bp.route('/')
def index(response=None):
    data, status =listStudent()
    if(status==200):
        return render_template("students/index.html", students=data, response=response)
    else:
        return data

@bp.route('/add/', methods=['POST'])
def add():
    if request.method == 'POST':
        response = saveStudent(form=request.form)
        return index(response=response)

@bp.route('/add/')
def form():
    return render_template("students/form.html")