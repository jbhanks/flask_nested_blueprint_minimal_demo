from flask import Blueprint
app2_bp = Blueprint(
    'app2_bp', __name__,
    template_folder='templates',
    static_folder='static'
)
