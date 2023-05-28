from flask import Blueprint

bp = Blueprint("programs", __name__)

from app.main.blueprint.programs import routes