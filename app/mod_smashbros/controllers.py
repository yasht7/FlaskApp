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
def index():
    # fectch all characters
    characters=Character.query.all()
    return render_template('smashbros/index.html', characters=characters)

@mod_smashbros.route('/add_character', methods=['GET', 'POST'])
def add_smashbro():
    # print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    form = NewCharacterForm(request.form)

    if request.method == "POST" and form.validate():
        # register smashbros
        name = form.name.data
        weight = int(form.weight.data)
        powers = form.powers.data
        speed = int(form.speed.data)
        character = Character(name, weight, powers, speed)
        db.session.add(character)
        db.session.commit()
        return redirect(url_for('smashbros.index'))
    return render_template("smashbros/add_character.html", form=form)
