from flask import Flask, request, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import pbkdf2_sha256

from wtform_registro import *
from modelos import *

app = Flask(__name__)
app.secret_key = 'replace later'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://mciebhbvvwkyje:8c7c356e012a9348f9e5257b90e5bad7b0f60085da2f292420464b2edf0abace@ec2-52-5-176-53.compute-1.amazonaws.com:5432/dbor0jn7c62572'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  

db = SQLAlchemy(app)

@app.route("/", methods=['GET', 'POST'])
def index():

    reg_form = Registro()
    if reg_form.validate_on_submit():

        usuario = reg_form.usuario.data
        contrasena = reg_form.contrasena.data
        nombre = reg_form.nombre.data
        apellido = reg_form.apellido.data
        edad = reg_form.edad.data
        genero = reg_form.genero.data

        hashed_pswd = pbkdf2_sha256.hash(contrasena)

        
        with app.app_context():     
            user = User(nombre=nombre, apellido=apellido, usuario=usuario, contrasena=hashed_pswd, edad=edad, genero=genero)                  
            db.create_all() 
            db.session.add(user)
            db.session.commit()
            
        return redirect(url_for('inicio'))   

    return render_template("index.html", form=reg_form)

@app.route("/inicio", methods=['GET','POST'])
def inicio():

    inicio_form = InicioSesion()

    if inicio_form.validate_on_submit():
        return "Haz iniciado sesion"

    return render_template("inicio.html",  form=inicio_form)    

    

if __name__ == "__main__":

    db.init_app(app)
    app.run(debug=True)