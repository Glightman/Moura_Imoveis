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
        print('entrei no read_single')
        lista_users1 = users
        for user in lista_users1:
            print(user.name)
            if user.email == email and user.password == password:
                print(user.name)
                return Users.query.get(user.id)

class Imovel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
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

    def __init__(self, user_id, status, category, prop_state, space, banheiros, quartos, cidade, bairro, views, data_cadastro, price, rua, area):
        self.user_id = user_id
        self.status = status
        self.category = category
        self.prop_state = prop_state
        self.space = space
        self.banheiros = banheiros
        self.quartos = quartos
        self.cidade = cidade
        self.bairro = bairro
        self.views = views
        self.data_cadastro = data_cadastro
        self.price = price
        self.rua = rua
        self.area = area
    
    @staticmethod
    def read_imovel():
        return Imovel.query.order_by(Imovel.id).all()

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
        print('entrei no post')
        form = request.form
        user = Users.read_single(form['email'], form['password'])
        print(form['email'], form['password'])
        email = form['email']
        password = form['password']
        if user:
            print('cheguei no redirect')
            return redirect('/admin')
    return render_template('login.html', email=email, password=password)

@bp.route('/imovel_registration')
def imovel_register():
    return render_template('imovel_register.html')

@bp.route('/admin')
def admin():
    return render_template('admin.html')

app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(debug=True)
