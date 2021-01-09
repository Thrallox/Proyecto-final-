from flask import Flask

myapp = Flask(__name__, instance_relative_config=True)
myapp.config.from_object("config")

from crypto import views