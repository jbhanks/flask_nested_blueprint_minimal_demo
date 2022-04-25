"""Compile static assets."""
from flask import Flask, current_app as app
from flask_assets import Environment, Bundle


def compile_static_assets(assets):
    """Create stylesheet bundles."""
    assets = Environment(app)
    assets.auto_build = True
    assets.debug = False
    common_less_bundle = Bundle(
        'src/less/*.less',
        filters='less,cssmin',
        output='dist/css/style.css',
        extra={'rel': 'stylesheet/less'}
    )
    home_less_bundle = Bundle(
            'home_bp/less/home.less',
            filters='less,cssmin',
            output='dist/css/home.css',
            extra={'rel': 'stylesheet/less'})
    app1_less_bundle = Bundle(
            'app1_bp/less/app1.less',
            filters='less,cssmin',
            output='dist/css/app1.css',
            extra={'rel': 'stylesheet/less'})
    app2_less_bundle = Bundle(
            'app2_bp/less/app2.less',
            filters='less,cssmin',
            output='dist/css/app2.css',
            extra={'rel': 'stylesheet/less'})
    # End of bundle definitions
    assets.register('common_less_bundle', common_less_bundle)
    assets.register('home_less_bundle', home_less_bundle)
    assets.register('app1_less_bundle', app1_less_bundle)
    assets.register('app2_less_bundle', app2_less_bundle)
    # End of asset registration
    if app.config['FLASK_ENV'] == 'development':
        common_less_bundle.build()
        home_less_bundle.build()
        app1_less_bundle.build()
        app2_less_bundle.build()
        # End of bundle builds
    return assets
