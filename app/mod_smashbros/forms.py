from flask_wtf import Form # , RecaptchaField

from wtforms import Form, BooleanField, StringField, DecimalField, validators

class NewCharacterForm(Form):
    name = StringField('Character', [validators.Length(min=1, max=25)])
    weight = DecimalField('Weight', [validators.NumberRange(min=0, max=5)])
    powers = StringField('Powers')
    speed = DecimalField('Speed', [validators.NumberRange(min=0, max=5)])
