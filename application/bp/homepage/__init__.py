"""
homepage blueprint
"""

from flask import Blueprint, render_template

# Declare Blueprint object
homepage = Blueprint('homepage', __name__, template_folder='templates')

# Define the default route for the homepage
@homepage.route('/')
def home():
    """
    Render the homepage template.
    """
    return render_template('homepage.html')

# Define the about route
@homepage.route('/about')
def about():
    """
    Render the about page template.
    """
    return render_template('about.html')
