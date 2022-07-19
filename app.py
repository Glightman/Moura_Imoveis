from os import name
from flask import (Flask, Blueprint, render_template, request, session)
from http import server
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
bp = Blueprint('app', __name__)

user = 'gnstrfnl' 
database = 'gnstrfnl'
password = '6EzO7_Wb5AaCkQ6fPbVIL5sSyM6YYbSd' 
host = 'kesavan.db.elephantsql.com' 

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{database}' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secreta'
db = SQLAlchemy(app)

class Imovel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    prop_state_id = db.Column(db.Integer, db.ForeignKey('prop_state.id'))
    space_id_id = db.Column(db.Integer, db.ForeignKey('space.id'))
    banheiro = db.Column(db.Integer, nullable = False)
    quarto = db.Column(db.Integer, nullable = False)
    cidade = db.Column(db.String(25), nullable = False)
    bairro = db.Column(db.String(25), nullable = False)
    views = db.Column(db.Integer, nullable = False)
    data_cadastro = db.Column(db.DateTime, nullable = False)
    price = db.Column(db.Integer, nullable = False)

    def __init__(self, user_id, status_id, category_id, prop_state_id, space_id_id, banheiro, quarto, cidade, bairro, views, data_cadastro, price):
        self.user_id = user_id
        self.status_id = status_id
        self.category_id = category_id
        self.prop_state_id = prop_state_id
        self.space_id_id = space_id_id
        self.banheiro = banheiro
        self.quarto = quarto
        self.cidade = cidade
        self.bairro = bairro
        self.views = views
        self.data_cadastro = data_cadastro
        self.price = price
    
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

@bp.route('/')
def index():
    img_imovel = Img_imovel.read_img_imovel()
    imovel = Imovel.read_imovel()
    return render_template('teste.html', lista_img = img_imovel, lista_imovel = imovel)

app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(debug=True)

#results = db.session.query(Imovel, Img_imovel).join(Img_imovel).all()
#print(Imovel.bairro, Img_imovel.img_url)