from flask_wtf import Form # , RecaptchaField

from wtforms import Form, BooleanField, StringField, DecimalField, validators

class NewCharacterForm(Form):
    name = StringField('Character Name', [validators.Length(min=1, max=25)])
    weight = DecimalField('Weight', [validators.NumberRange(min=0, max=10000)])
    powers = StringField('Moves', [validators.Length(min=1, max=100)])
    speed = DecimalField('Speed', [validators.NumberRange(min=0, max=100)])
