from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo

class Registro(FlaskForm):

    nombres = StringField('nombres_label',
        validators=[InputRequired(message = "Requiere un nombre"),
        Length(min=0 , max=30, message="El nombre debe contener maximo 30 caracteres")])
   
    apellidos = StringField('apellidos_label',
        validators=[InputRequired(message = "Requiere un apellido"),
        Length(min=0 , max=30, message ="El apellido debe contener maximo 30 caracteres")])

    usuario = StringField('usuario_label',
        validators=[InputRequired(message="Requiere un nombre de usuario"),
        Length(min=4, max=25, message="El nombre de usuario debe tener entre 4 y 25 caracteres")])

    contraseña = PasswordField('contraseña_label',
        validators=[InputRequired(message="Requiere una contraseña"),
        Length(min=8, max=25, message="La contraseña debe tener entre 8 y 25 caracteres")])

    confirmar_contraseña = PasswordField('confirmar_contraseña_label',
        validators=[InputRequired(message="Requiere una contraseña"),
        EqualTo('contraseña', message="La contraseña debe coincidir")])

    edad = StringField('edad_label',
        validators=[InputRequired(message = "Requiere la edad"),
        Length(min=0 , max=2, message ="La edad debe contener maximo 2 caracteres")])  
        
    genero = StringField('genero_label',
        validators=[InputRequired(message = "Campo obligatorio *"),
        Length(min=0 , max=1, message= " Escribe F para femenino y M para masculino ")])  
       

    boton_registro = SubmitField('Registrarse')


