from flask import render_template, request
from app.main.blueprint.programs import bp

from ...controller.program_controller import savePrograms, listPrograms

# * /programs/

@bp.route('/')
def index(response=None):
    data, status =listPrograms()
    if(status==200):
        return render_template("programs/index.html", programs=data, response=response)
    else:
        return data

@bp.route('/add/', methods=['POST'])
def add():
    if request.method == 'POST':
        response = savePrograms(form=request.form)
        return index(response=response)

@bp.route('/add/')
def form():
    return render_template("programs/form.html")