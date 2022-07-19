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


#MODELO DO USUÁRIO
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name_ = db.Column(db.String(60), nullable = False)
    birthday = db.Column(db.Date, nullable = False)
    password = db.Column(db.String(10), nullable = False)
    role = db.Column(db.String(25), nullable = False)
    email = db.Column(db.String(120), nullable = False)
    phone_number = db.Column(db.String(25), nullable = False)

    def __init__(self, name_, birthday, password, role, email, phone_number):
        self.name_ = name_
        self.birthday = birthday
        self.password = password
        self.role = role
        self.email = email
        self.phone_number = phone_number

#MODELO DO IMÓVEL
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
    def read_all_imovel():
        return Imovel.query.join(Img_imovel, Imovel.id == Img_imovel.imovel_id).order_by(Imovel.price)

#MODELO DAS FOTOS DOS IMOVEIS
class Img_imovel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    imovel_id = db.Column(db.Integer, db.ForeignKey('imovel.id'))
    img_url = db.Column(db.String(1000), nullable = False)

    def __init__(self, imovel_id, img_url):
        self.imovel_id = imovel_id
        self.img_url = img_url

#MODELO DAS FOTOS DO USUÁRIO
class Img_user(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    img_url = db.Column(db.String(1000), nullable = False)

    @staticmethod
    def read_all_img_imovel():
        return Img_imovel.query.order_by(Img_imovel.id).all()
    
    @staticmethod
    def read_single(pacientes_id):
        return User.query.get(pacientes_id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, new_data):
        self.name_ = new_data.name_
        self.idade = new_data.idade
        self.estado = new_data.estado
        self.sexo = new_data.sexo
        self.dose = new_data.dose
        self.save()

    def delete(self):
        db.session.delete(self) 
        db.session.commit()


def send_email(name, email, phone):
    host = "smtp.office365.com"
    port = "587"
    login = "blakewebassociation@outlook.com"
    senha = "Kaga@2019"
    name = name
    email = email
    phone = phone

    server = smtplib.SMTP(host, port)

    server.ehlo()
    server.starttls()
    server.login(login, senha)

    corpo = f'''
    Nome: {name}
    Email: {email}
    Número de telefone: {phone}'''
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = "rezbosa@gmail.com"
    email_msg['Subject'] = "Matheus você tem um novo cliente"
    email_msg.attach(MIMEText(corpo, 'plain'))

    server.sendmail(email_msg["From"], email_msg["To"], email_msg.as_string())

    server.quit()



@app.route('/')
def index():
    imoveis = Imovel.read_all_imovel()
    return render_template('index.html', lista_imoveis = imoveis)

if __name__ == '__main__':
    app.run(debug=True)