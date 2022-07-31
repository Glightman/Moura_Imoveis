from collections import UserDict
from os import name
from flask import (Flask, Blueprint, redirect, render_template, request, session, url_for)
from http import server
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
bp = Blueprint('app', __name__)

user = 'rteecfaw' 
database = 'rteecfaw'
password = 'gvLty8KzziKKxndohV0nF_rGlbGJftJ1' 
host = 'tuffi.db.elephantsql.com' 

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{database}' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secreta'
db = SQLAlchemy(app)

#MODELO DO USUÁRIO
class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(60), nullable = False)
    birthday = db.Column(db.Date, nullable = False)
    password = db.Column(db.String(10), nullable = False)
    role = db.Column(db.String(25), nullable = False)
    email = db.Column(db.String(120), nullable = False)
    phone_number = db.Column(db.String(25), nullable = False)

    def __init__(self, name, birthday, password, role, email, phone_number):
        self.name = name
        self.birthday = birthday
        self.password = password
        self.role = role
        self.email = email
        self.phone_number = phone_number
    
    @staticmethod
    def read_user():
        return Users.query.order_by(Users.id).all()
    
    @staticmethod
    def read_single(email, password):
        users = Users.read_user()
        lista_users1 = users
        for user in lista_users1:
            if user.email == email and user.password == password:
                return Users.query.get(user.id)

class Imovel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    status = db.Column(db.String(250), nullable = False)
    category = db.Column(db.String(250), nullable = False)
    prop_state = db.Column(db.String(250), nullable = False)
    space = db.Column(db.String(250), nullable = False)
    banheiros = db.Column(db.Integer, nullable = False)
    quartos = db.Column(db.Integer, nullable = False)
    cidade = db.Column(db.String(25), nullable = False)
    bairro = db.Column(db.String(25), nullable = False)
    views = db.Column(db.Integer, nullable = False)
    data_cadastro = db.Column(db.Date, nullable = False)
    price = db.Column(db.Integer, nullable = False)
    rua = db.Column(db.String(120), nullable = False)
    area = db.Column(db.Integer, nullable = False)

    def __init__(self, user_id, status, category, prop_state, space, banheiros, quartos, cidade, bairro, data_cadastro, price, rua, area):
        self.user_id = user_id
        self.status = status
        self.category = category
        self.prop_state = prop_state
        self.space = space
        self.banheiros = banheiros
        self.quartos = quartos
        self.cidade = cidade
        self.bairro = bairro
        self.views = 0
        self.data_cadastro = data_cadastro
        self.price = price
        self.rua = rua
        self.area = area
    
    @staticmethod
    def read_imovel():
        return Imovel.query.order_by(Imovel.id).all()

    @staticmethod
    def read_single(imovel_id):
        return Imovel.query.get(imovel_id)
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self) 
        db.session.commit()

class Img_imovel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    imovel_id = db.Column(db.Integer, db.ForeignKey('imovel.id'))
    img_url = db.Column(db.String(1000), nullable = False)

    def __init__(self, imovel_id, img_url):
        self.imovel_id = imovel_id
        self.img_url = img_url

    @staticmethod
    def read_img_imovel():
        return Img_imovel.query.order_by(Img_imovel.id).all()
    
class Img_user(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    img_url = db.Column(db.String(1000), nullable = False)

    def __init__(self, user_id, img_url):
        self.user_id = user_id
        self.img_url = img_url

    @staticmethod
    def read_img_user():
        return Img_user.query.order_by(Img_user.id).all()

@bp.route('/')
def index():
    img_imovel = Img_imovel.read_img_imovel()
    imovel = Imovel.read_imovel()
    img_user = Img_user.read_img_user()
    user = Users.read_user()
    return render_template('index.html', lista_img = img_imovel, lista_imovel = imovel, lista_img_user = img_user, lista_user = user)

@bp.route('/login', methods=('GET','POST'))
def login():
    email = None
    password = None
    if request.method == 'POST':
        form = request.form
        user = Users.read_single(form['email'], form['password'])
        email = form['email']
        password = form['password']
        if user:
            return redirect(f'/admin/{user.name}{user.email}{user.id}')
    return render_template('login.html', email=email, password=password)

@bp.route('/create', methods=('GET','POST'))
def create():
    id_atribuido = None
    if request.method =='POST':
        form = request.form
        imovel = Imovel(2,
        form['status'], 
        form['category'], 
        form['prop_state'], 
        form['space'], 
        form['banheiros'], 
        form['quartos'], 
        form['cidade'], 
        form['bairro'], 
        form['data_cadastro'], 
        form['price'], 
        form['rua'], 
        form['area'])
        imovel.save()
        print('criei o imovel')
        id_atribuido=imovel.id
    return render_template('imovel_register.html', id_atribuido = id_atribuido)

@bp.route('/admin/<email>')
def admin(email):
    img_imovel = Img_imovel.read_img_imovel()
    imovel = Imovel.read_imovel()
    users = Users.read_user()
    lista_users2 = users

    for user in lista_users2:
        if user.email == 'vitors-dm@hotmail.com':
            if f'{user.name}{user.email}{user.id}' == email:
                return render_template('admin.html', lista_img = img_imovel, lista_imovel = imovel)
            else:
                return 'USUÁRIO NÃO ENCONTRADO!'

@bp.route('/delete/<imovel_id>')
def delete(imovel_id):
    imovel = Imovel.read_single(imovel_id)
    return render_template('delete.html', imovel = imovel)

@bp.route('/delete/<imovel_id>/confirmed')
def delete_confirmed(imovel_id):
    sucesso = None
    imovel =Imovel.read_single(imovel_id)
    if imovel:
        imovel.delete()
        sucesso=True
    return render_template('delete.html', sucesso = sucesso)

app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(debug=True)
