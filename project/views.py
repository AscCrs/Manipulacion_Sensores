from flask import render_template, Blueprint, request
from project import dataSensor, relayControl

content = Blueprint('content', __name__)

@content.route('/')
def index():
    temp = dataSensor.read_temp()
    return render_template('index.html', temp=temp)

@content.route('/relay', methods=['POST'])
def relay():
    relay_index = int(request.form['relay_index'])
    relay_state = int(request.form['relay_state'])
    relayControl.set_relay_state(relay_index, relay_state)
    return 'OK'