from flask import Blueprint, render_template, request

pages = Blueprint(__name__, "pages")

@pages.route('/')
def home():
    return render_template('doodleHome.html')