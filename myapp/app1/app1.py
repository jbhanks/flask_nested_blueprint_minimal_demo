from flask import Blueprint, render_template
from flask import current_app as app

# Blueprint Configuration
app1_bp = Blueprint('app1_bp', __name__,
                    template_folder='templates',
                    static_folder='static')


@app1_bp.route('/app1', methods=['GET'])
def app1():
    return render_template('app1.html',
                           title='Skeleton Site',
                           subtitle='Homepage',
                           template='app1-template')

