"""Initialize Flask app."""
from flask import Blueprint, Flask, url_for
from .app1 import app1

#from flask import Flask, redirect, url_for
#from . import config

from flask_assets import Environment

bp = Blueprint('main', __name__)

def create_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    assets = Environment()
    assets.init_app(app)
    with app.app_context():
        # Import parts of our application
        from .assets import compile_static_assets
        from .home import home
        from .app1 import app1
        from .app2 import app2
        # End of imports
        # Register Blueprints
        app.register_blueprint(home.home_bp)
        app1.app1_bp.register_blueprint(app1.subapp1a.subapp1a_bp, url_prefix='/subapp1a')
        bp.register_blueprint(app1.app1_bp, url_prefix='/app1')
        app.register_blueprint(bp)
        #app.register_blueprint(app1.app1_bp, url_prefix='/app1')
        #app1_bp.register_blueprint(subapp1a_bp, url_prefix='/subapp1a')
        app.register_blueprint(app2.app2_bp)
        # End of bp registration
        # Compile
        compile_static_assets
        return app



#app1.app1_bp.register_blueprint(app1.subapp1a.subapp1a_bp, url_prefix='/subapp1a')
#bp.register_blueprint(app1.app1_bp, url_prefix='/app1')
#app.register_blueprint(bp)
