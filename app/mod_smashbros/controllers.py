# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db

# Import Smashbro Form
from app.mod_smashbros.forms import NewCharacterForm

# Import Smashbro Model
from app.mod_smashbros.models import Character

# define the blue Blueprint
mod_smashbros = Blueprint('smashbros', __name__, url_prefix='/smashbros')

@mod_smashbros.route('/')
def show_main():
    render_template('index.html')

@mod_smashbros.route('/add_character')
def add_smashbro():
    form = NewCharacterForm(request.form)

    if form.validate_on_submit():
        # register smashbros
        pass

    return render_template("smashbros/index.html")
