from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html", current_page='home')
@views.route('/features')
def features():
    return render_template("features.html", current_page='Features')

@views.route('/contact')
def contact():
    return render_template("contact.html", current_page='Contact')

@views.route('/review')
def review():
    return render_template("review.html", current_page='Review')

@views.route('/about')
def about():
    return render_template("about.html", current_page='about')
