from flask import  Blueprint, Flask, url_for, render_template
from flask import current_app as app
from myapp.app1.subapp1a import subapp1a

# Blueprint Configuration
app1_bp = Blueprint('app1_bp', __name__,
                    template_folder='templates',
                    static_folder='static')


@app1_bp.route('/', methods=['GET'])
def app1():
    return render_template('app1.html',
                           title='Skeleton Site',
                           subtitle='Homepage',
                           template='app1-template')

