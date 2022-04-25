from flask import Flask, current_app as app1
from flask_assets import Environment, Bundle


def compile_static_assets(assets):
    """Create stylesheet bundles."""
    assets = Environment(app1)
    assets.auto_build = True
    assets.debug = False
    common_less_bundle = Bundle(
        'src/less/*.less',
        filters='less,cssmin',
        output='dist/css/style.css',
        extra={'rel': 'stylesheet/less'}
    )
    subapp1a_less_bundle = Bundle(
            'subapp1a_bp/less/subapp1a.less',
            filters='less,cssmin',
            output='dist/css/subapp1a.css',
            extra={'rel': 'stylesheet/less'})
    # End of bundle definitions
    assets.register('common_less_bundle', common_less_bundle)
    assets.register('subapp1a_less_bundle', subapp1a_less_bundle)
    # End of asset registration
    if app1.config['FLASK_ENV'] == 'development':
        common_less_bundle.build()
        subapp1a_less_bundle.build()
        # End of bundle builds
    return assets
