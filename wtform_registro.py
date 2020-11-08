from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
from modelos import User
from passlib.hash import pbkdf2_sha256



def invalid_credentials(form, field):
    
    usuario_entered = form.usuario.data
    contrasena_entered = field.data


    user_object = User.query.filter_by(usuario=usuario_entered).first()
    if user_object is None:
        raise ValidationError("Usuario o contraseña incorrecto")
    elif not pbkdf2_sha256.verify(contrasena_entered, user_object.contrasena):
        raise ValidationError("Usuario o Contraseña incorrecto")



class Registro(FlaskForm):
    '''Registratio form'''

    usuario = StringField('usuario_label',
        validators=[InputRequired(message="Escribe un nombre de usuario"),
        Length(min=4, max=25, message="El nombre de usuario debe tener entre 4 y 25 caracteres")])

    contrasena = PasswordField('contrasena_label',
        validators=[InputRequired(message="Escribe una contraseña"),
        Length(min=8, max=25, message="La contraseña debe tener entre 8 y 25 caracteres")])

    confirmar_contrasena = PasswordField('confirmar_contraseña_label',
        validators=[InputRequired(message="Escribe una contraseña"),
        EqualTo('contrasena', message="Las contraseñas deben coincidir")])

    nombre = StringField('nombre_label',
        validators=[InputRequired(message = "Escribe tu nombre"),
        Length(min=0 , max=30, message="El nombre debe contener maximo 30 caracteres")])
   
    apellido = StringField('apellido_label',
        validators=[InputRequired(message = "Escribe tu apellido"),
        Length(min=0 , max=30, message="El apellido debe contener maximo 30 caracteres")])

    edad = StringField('edad_label',
        validators=[InputRequired(message = "Escribe tu edad")])  
        
    genero = StringField('genero_label',
        validators=[InputRequired(message = "Escribe tu genero"),
        Length(min=0 , max=1, message="Escribe (F) para femenino y (M) para masculino ")])     

    boton_registro = SubmitField('Registrarse')

    def validate_usuario(self, usuario):
        user_object = User.query.filter_by(usuario=usuario.data).first()
        if user_object:
            raise ValidationError("El usuario ya existe. Elige otro nombre de usuario")

class InicioSesion(FlaskForm):

    usuario = StringField ('usuario_label',
         validators=[InputRequired(message="Usuario requerido")])   

    contrasena = PasswordField('contrasena_label',
         validators= [InputRequired(message="Contraseña requerida"),
         invalid_credentials])

    boton_inicio = SubmitField('Inicio')         