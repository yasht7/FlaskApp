# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
import sqlalchemy
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
    # TODO: add limit on fetch
    characters=Character.query.all()
    return render_template('smashbros/index.html', characters=characters)


# Character page
@mod_smashbros.route('/character/<string:id>')
def character(id):
    character = Character.query.get(id)
    return render_template('smashbros/character.html', character=character)


# Adding new character
@mod_smashbros.route('/add_character', methods=['GET', 'POST'])
def add_smashbro():
    form = NewCharacterForm(request.form)
    # try catch
    if request.method == "POST" and form.validate():
        # register smashbros
        name = form.name.data
        weight = int(form.weight.data)
        powers = form.powers.data
        speed = int(form.speed.data)
        character = Character(name, weight, powers, speed)
        db.session.add(character)
        try:
            db.session.commit()
            return redirect(url_for('smashbros.index'))
        except sqlalchemy.exc.IntegrityError as e:
            flash("Character name already exists, could not add!")
            return render_template("smashbros/add_character.html", form=form)
        finally:
            db.session.close()
    return render_template("smashbros/add_character.html", form=form)



# Updating the character
@mod_smashbros.route('/update_character/<string:id>', methods=['GET', 'POST'])
def update_character(id):
    character = Character.query.get(id)

    # populate fields with current data
    form = NewCharacterForm(request.form)
    form.name.data = character.name
    form.weight.data = character.weight
    form.powers.data = character.powers
    form.speed.data = character.speed

    if request.method == 'POST':
        character.name = request.form['name']
        character.weight = request.form['weight']
        character.powers = request.form['powers']
        character.speed = request.form['speed']
        db.session.commit()
        flash('Udpate Done!', 'success')
        return redirect(url_for('smashbros.index'))
    return render_template("smashbros/udpate_character.html", form=form)


# Deleting the character
@mod_smashbros.route('/delete_character/<string:id>', methods=['POST'])
def delete_character(id):
    character = Character.query.get(id)
    db.session.delete(character)
    db.session.commit()
    return redirect(url_for('smashbros.index'))
