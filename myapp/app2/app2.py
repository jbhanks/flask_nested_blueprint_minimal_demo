from flask import Blueprint, render_template
from flask import current_app as app

# Blueprint Configuration
app2_bp = Blueprint('app2_bp', __name__,
                    template_folder='templates',
                    static_folder='static')


@app2_bp.route('/app2', methods=['GET'])
def app2():
    return render_template('app2.html',
                           title='Skeleton Site',
                           subtitle='Homepage',
                           template='app2-template')

