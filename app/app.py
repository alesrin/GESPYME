from flask import Flask, render_template, redirect, url_for, flash, request, json
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import DataRequired, Length, ValidationError
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt
import os
from flask_login import LoginManager, login_user, current_user, logout_user, UserMixin





app = Flask(__name__)
app.config['SECRET_KEY'] = '90bc04947dce3a57edbd90fefbc1c3d0211739937a6fc5ed'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

def init_app():
    with app.app_context():
        db.create_all()



#Cargamos los archivos json
data_proyecto = 'data_proyecto.json'


#Creamos las clases que necesitamos
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    role = RadioField('Role', choices=[('administrador', 'Administrador'), ('manager', 'Manager'), ('worker', 'Worker')], validators=[DataRequired()])
    submit = SubmitField('Guardar')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is already taken. Please choose a different one.')


class User(UserMixin, db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'manager' or 'worker' or 'administrador'

    def __init__(self, username, role):
        self.username = username
        self.role = role
        
    
    def __repr__(self) -> str:
        return f"<User {self.username}>"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    

login_manager = LoginManager(app)
login_manager.login_view = 'inicio'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#PROYECTOS

class Tarea:
    #definimos un metodo constructor
    def __init__(self, id_tarea : str, nombre_tarea : str, tiempo_estimado : int, fecha_inicio : dt, fecha_fin : dt,
                 fecha_limite : dt, coste_tarea : float, estado_tarea: bool ,id_proyecto: str, trabajadores: list):
        self.id_tarea = id_tarea
        self.nombre_tarea = nombre_tarea
        self.tiempo_estimado = tiempo_estimado
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.fecha_limite = fecha_limite
        self.coste_tarea = coste_tarea
        self.estado_tarea = estado_tarea
        self.id_proyecto = id_proyecto
        self.trabajadores = trabajadores

class Proyecto:
    def __init__(self, id_proyecto, nombre_proyecto, manager_proyecto, empleados, tareas):
        self.id_proyecto = id_proyecto
        self.nombre_proyecto = nombre_proyecto
        self.manager_proyecto = manager_proyecto
        self.empleados = empleados  # Lista de empleados asociados al proyecto
        self.tareas = tareas  # Lista de tareas del proyecto

    @classmethod
    def from_dict(cls, data):
        id_proyecto = data.get('id_proyecto')
        nombre_proyecto = data.get('nombre_proyecto')
        manager_proyecto = data.get('manager_proyecto')
        empleados = data.get('empleados', [])  # Lista de empleados asociados al proyecto
        tareas = data.get('tareas', [])  # Lista de tareas asociadas al proyecto
        return cls(id_proyecto, nombre_proyecto, manager_proyecto, empleados, tareas)
    
    @classmethod
    def cargar_proyectos(cls):
        # Verificar si el archivo JSON existe
        if not os.path.exists(data_proyecto):
            # Archivo no encontrado, crear el archivo con datos iniciales
            datos_iniciales = [
                {
                    "id_proyecto": "P1",
                    "nombre_proyecto": "Proyecto 1",
                    "manager_proyecto": "UM1",
                    "empleados": [],  # Lista de empleados inicialmente vacía
                    "tareas": ["T1", "T2"]
                }
            ]

            # Escribir los datos iniciales en el archivo JSON
            with open(data_proyecto, 'w') as file:
                json.dump(datos_iniciales, file, indent=4)

        # Cargar los proyectos desde el archivo JSON
        with open(data_proyecto, 'r') as json_file:
            proyecto_data = json.load(json_file)
            proyectos = []
            for proyecto_data in proyecto_data:
                # Crear un objeto Proyecto utilizando los datos del archivo JSON
                proyecto = cls(
                    proyecto_data['id_proyecto'],
                    proyecto_data['nombre_proyecto'],
                    proyecto_data['manager_proyecto'],
                    proyecto_data['empleados'],  # Lista de empleados
                    proyecto_data['tareas']  # Lista de tareas
                )
                proyectos.append(proyecto)
            return proyectos

    
    def guardar_proyectos(proyectos):
        proyectos_data = [proyecto.to_dict() for proyecto in data_proyecto]
        with open(data_proyecto, 'w') as json_file:
            json.dump(proyectos_data, json_file, indent=4)
    

def cargar_proyectos():
    if not os.path.exists(data_proyecto):
        # Código para manejar la creación del archivo JSON si no existe
        return []

    with open(data_proyecto, 'r') as json_file:
        proyecto_data = json.load(json_file)
        proyectos = []
        for proyecto_info in proyecto_data:
            proyecto = Proyecto.from_dict(proyecto_info)
            proyectos.append(proyecto)
        return proyectos

# Ejemplo de uso
proyectos = cargar_proyectos()
print(proyectos)

# Guardar datos de películas en data.json
def guardar_proyectos(proyectos):
    proyectos_data = [proyecto.to_dict() for proyecto in proyectos]
    with open(data_proyecto, 'w') as json_file:
        json.dump(proyectos_data, json_file, indent=4)

@app.route('/proyecto/<tipo>', methods=['GET'])
def proyecto(tipo):
    proyectos = cargar_proyectos()
    proyectos_tipo = [p for p in proyectos if p.nombre_proyecto == tipo]
    return render_template('proyectos.html', proyectos=proyectos_tipo, tipo=tipo)

@app.route('/inicio', methods=['GET', 'POST'])
def index():
    usuario = User.query.all()
    proyectos = cargar_proyectos()
    return render_template("index.html", proyectos=proyectos, usuario=usuario)

@app.route('/', methods=['GET', 'POST'])
def inicio_sesion():
    init_app()
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('index'))
        else:
            flash('Usuario o contraseña inválidos.', 'danger')
    return render_template('login.html', form=form)

@app.route('/crear_admin', methods=['GET', 'POST'])
def crear_admin():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, role=form.role.data)
        user.set_password(form.password.data) 
        db.session.add(user)
        db.session.commit()
        return user
    return render_template('anadir_administrador_manager.html', form=form)


@app.route('/cerrar-sesion')
def logout():
    logout_user()
    return redirect(url_for('inicio_sesion'))


@app.route('/usuarios', methods=['GET', 'POST'])
def mostrar_usuarios():
    # Obtener todos los usuarios de la base de datos
    usuarios = User.query.all()
    return render_template('usuarios.html', usuarios=usuarios)



if __name__ == '__main__':
    
    app.run(debug=True)