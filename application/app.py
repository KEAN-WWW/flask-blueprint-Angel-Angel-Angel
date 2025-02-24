"""
 Flask application
"""

from flask import Flask
from application.bp.homepage import homepage

# Create the Flask app
app = Flask(__name__)

# Register the homepage blueprint with a URL prefix
app.register_blueprint(homepage, url_prefix='/homepage')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
