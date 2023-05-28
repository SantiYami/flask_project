from flask import Blueprint

bp = Blueprint("students", __name__)

from app.main.blueprint.students import routes