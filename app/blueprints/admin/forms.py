from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileSize
from wtforms import StringField, BooleanField, SubmitField, DecimalField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length


class FormCategoria(FlaskForm):
    nombre = StringField('Nombre',
                validators=[DataRequired(), Length(min=2, max=80)])

    descripcion = StringField('Descripción',
                validators=[Length(max=200)])

    activa = BooleanField('Activa')

    submit = SubmitField('Guardar')


class FormProducto(FlaskForm):
    nombre = StringField('Nombre',
                validators=[DataRequired(), Length(min=2, max=150)])

    descripcion = StringField('Descripción')

    precio = DecimalField('Precio',
                validators=[DataRequired()])

    stock = IntegerField('Stock',
                validators=[DataRequired()])

    categoria_id = SelectField('Categoría', coerce=int, validators=[DataRequired()])

    imagen = FileField('Imagen', validators=[
        FileAllowed(['jpg', 'jpeg', 'webp'], 'Solo se permiten imágenes JPG, JPEG o WEBP.'),
        FileSize(max_size=2 * 1024 * 1024, message='La imagen no debe superar los 2MB.')
    ])

    activo = BooleanField('Activo')

    submit = SubmitField('Guardar')