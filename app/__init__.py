from flask import Flask, render_template, request, url_for, redirect
from .config import Config

from .extensions import db

def create_app():
    app = Flask(__name__)
    with app.app_context():
        app.config.from_object(Config)
        
        db.init_app(app)
        from .main.models.student import Student
        from .main.models.program import Program
        from .main.models.course import Course
        from .main.models.student_course import StudentCourse
        
        db.create_all()
        
        from app.main import bp as main_blueprint
        from app.main.blueprint.students import bp as students_blueprint
        from app.main.blueprint.programs import bp as programs_blueprint
        
        
        app.register_blueprint(main_blueprint)
        app.register_blueprint(students_blueprint, url_prefix="/students")
        app.register_blueprint(programs_blueprint, url_prefix="/programs")
        
        
        @app.errorhandler (404)
        def page_not_found (e):
            return render_template ('404.html'), 404
        
        return app