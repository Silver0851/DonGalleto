from flask import Blueprint, jsonify, request, render_template

import traceback

main = Blueprint('index_blueprint', __name__)

@main.route('/')
def index():
    return render_template('layout/base.html')

@ main.route('/alerts')
def alerts():
    return render_template('examples/elements-alerts.html')

