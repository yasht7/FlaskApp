# Import flask and template operators
from flask import Flask, render_template, redirect, url_for

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for('smashbros.index'))

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


# Internal server error handler
@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_auth.controllers import mod_auth as auth_module

from app.mod_smashbros.controllers import mod_smashbros as smashbros_module

# Register blueprint(s)
app.register_blueprint(auth_module)
app.register_blueprint(smashbros_module)

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
