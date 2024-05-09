from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, login_user, logout_user, UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import DataRequired, Length, ValidationError
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import json
from models.proyecto import Proyecto





app = Flask(__name__)
app.config['SECRET_KEY'] = '90bc04947dce3a57edbd90fefbc1c3d0211739937a6fc5ed'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

#Cargamos los archivos json
data_proyecto = '/Datos/data_proyecto.json'
data_usuarios = '/Datos/data_usuarios.json'
data_usuarios_administrador = '/Datos/data_usuarios_administrador.json'
data_usuarios_manager = '/Datos/data_usuarios_manager.json'
data_usuarios_worker = '/Datos/data_usuarios_worker.json'


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    nombre = StringField('Nombre', validators=[DataRequired()])
    role = RadioField('Role', choices=[('administrador', 'Administrador'), ('manager', 'Manager')], validators=[DataRequired()])
    telefono = StringField('Teléfono', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    horas_semanales = StringField('Horas Semanales', validators=[DataRequired()])
    coste_hora = StringField('Coste por Hora', validators=[DataRequired()])
    puesto_trabajo = StringField('Puesto de Trabajo', validators=[DataRequired()])
    submit = SubmitField('Guardar')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is already taken. Please choose a different one.')
        
class User(UserMixin, db.Model):
    __tablename__ = 'users'

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
    
class Trabajador(db.Model):
    __tablename__ = 'workers'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    horas_semanales = db.Column(db.Integer, nullable=False)
    coste_hora = db.Column(db.Float, nullable=False)
    puesto_trabajo = db.Column(db.String(100), nullable=False)

    def __init__(self, nombre, usuario_id, telefono, email, horas_semanales, coste_hora, puesto_trabajo):
        self.nombre = nombre
        self.usuario_id = usuario_id
        self.telefono = telefono
        self.email = email
        self.horas_semanales = horas_semanales
        self.coste_hora = coste_hora
        self.puesto_trabajo = puesto_trabajo


login_manager = LoginManager(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



@app.route('/inicio', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    return render_template("index.html", form=form)

@app.route('/', methods=['GET', 'POST'])
def login():
    db.create_all()
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Has iniciado sesión correctamente.', 'success')
            next_page = request.args.get('next')
            return redirect(next_page or url_for('index'))
        else:
            flash('Usuario o contraseña inválidos.', 'danger')
    return render_template('login.html', form=form)

# Ruta para el formulario de creación de administrador/manager
@app.route('/crear_admin', methods=['GET', 'POST'])
def crear_admin():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Crear usuario
        hashed_password = generate_password_hash(form.password.data)
        user = User(username=form.username.data, password=hashed_password, role=form.role.data)
        db.session.add(user)
        db.session.commit()

        # Crear trabajador asociado
        trabajador = Trabajador(
            nombre=form.nombre.data,
            usuario_id=user.id,
            telefono=form.telefono.data,
            email=form.email.data,
            horas_semanales=form.horas_semanales.data,
            coste_hora=float(form.coste_hora.data),
            puesto_trabajo=form.puesto_trabajo.data
        )
        db.session.add(trabajador)
        db.session.commit()

        flash('Usuario y trabajador creados correctamente.', 'success')
        return redirect(url_for('index'))  # Redireccionar a la misma página después de registrar

    return render_template('crear_administrador.html', form=form)

@app.route('/cerrar-sesion')
def logout():
    logout_user()
    return redirect(url_for('login'))

""" @app.route('/menu_worker')
def menu_worker():
    if current_user.is_authenticated and current_user.role == 'worker':
        return 'Página de inicio para usuarios worker'
    else:
        flash('Debe iniciar sesión como usuario worker para acceder a esta página.', 'warning')
        return redirect(url_for('index'))

@app.route('/menu_manager')
def menu_manager():
    if current_user.is_authenticated and current_user.role == 'manager':
        return 'Página de inicio para usuarios manager'
    else:
        flash('Debe iniciar sesión como usuario manger para acceder a esta página.', 'warning')
        return redirect(url_for('index'))

@app.route('/menu_admin')
def menu_administrador():
    if current_user.is_authenticated and current_user.role == 'administrador':
        return 'Página de inicio para usuarios administrador'
    else:
        flash('Debe iniciar sesión como usuario administrador para acceder a esta página.', 'warning')
        return redirect(url_for('index')) """





if __name__ == '__main__':
    app.run(debug=True)