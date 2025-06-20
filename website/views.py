from flask import Blueprint, render_template
from flask_login import current_user

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html", current_page='home', user=current_user)

@views.route('/features')
def features():
    return render_template("features.html", current_page='Features', user=current_user)

@views.route('/contact')
def contact():
    return render_template("contact.html", current_page='Contact', user=current_user)

@views.route('/review')
def review():
    return render_template("review.html", current_page='Review', user=current_user)

@views.route('/about')
def about():
    return render_template("about.html", current_page='about', user=current_user)

@views.route('/collections')
def collections():
    return render_template("collections.html", current_page='collections', user=current_user)
