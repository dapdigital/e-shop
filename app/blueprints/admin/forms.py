from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class FormCategoria(FlaskForm):
    nombre = StringField('Nombre',
                validators=[DataRequired(), Length(min=2, max=80)])

    descripcion = StringField('Descripción',
                validators=[Length(max=200)])

    activa = BooleanField('Activa')

    submit = SubmitField('Guardar')        
    