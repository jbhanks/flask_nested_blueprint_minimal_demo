from flask import Blueprint, Flask, render_template
from flask import current_app as app


from flask import Blueprint

subapp1a_bp = Blueprint(
    'subapp1a', __name__,
    template_folder='templates',
    static_folder='static'
)


@subapp1a_bp.route('/', methods=['GET'])
def sub1a():
    return render_template('subapp1a.html',
                           title='Skeleton Site',
                           subtitle='subapp1a',
                           template='subapp1a-template')


