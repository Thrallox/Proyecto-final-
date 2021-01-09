from flask import render_template, request, url_for, redirect

from crypto import myapp

@myapp.route("/")
def index():
    return "Inicio"