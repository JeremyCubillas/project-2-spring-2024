"""
Main Flask Application Initialization
"""
from flask import Flask
from flask_migrate import Migrate
from application.database import db
import config
from application.bp.homepage import bp_homepage


migrate = Migrate()


def init_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config.Config())

    # Initialize Plugins
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():

        # Register Blueprints
        app.register_blueprint(bp_homepage)
        return app
