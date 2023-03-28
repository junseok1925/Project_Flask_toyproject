from flask import Blueprint, render_template

# 루트 
bp = Blueprint('artist', __name__, url_prefix='/artist')

@bp.route('/')
def index():
   return render_template('artist.html')
