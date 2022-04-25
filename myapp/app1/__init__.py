from flask import Blueprint


def create_app1():
    """Create Flask application."""
    app1 = Flask(__name__, instance_relative_config=False)
    app1.config.from_object('config.Config')
    assets = Environment()
    assets.init_app(app1)
    with app1.app_context():
        from .assets import compile_static_assets
        from .subapp1a import subapp1a
        # Register Blueprints
        app1.register_blueprint(subapp1a.subapp1a_bp)
        app.register_blueprint(app1.app1_bp)
        compile_static_assets
        return app



