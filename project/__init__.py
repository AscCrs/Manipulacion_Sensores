from flask import Flask

content = Flask(__name__)

from project.views import content

content.register_blueprint(content)