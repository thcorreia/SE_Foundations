# file with the blueprints
#my original file is called pages 

from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/") #homepage route
def home():
    return render_template("home.html")  