from flask import Blueprint, render_template
from flask import current_app as app


dfgfdgdf


from flask import Blueprint

subapp1a_bp = Blueprint(
    'subapp1a_bp', __name__,
    template_folder='templates',
    static_folder='static'
)



fdhgh

@subapp1a_bp.route('/app1/subapp1a', methods=['GET'])
def home():
    return render_template('subapp1a.html',
                           title='Skeleton Site',
                           subtitle='subapp1a',
                           template='subapp1a-template')


