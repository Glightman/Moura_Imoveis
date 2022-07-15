from flask import (Flask, Blueprint, render_template, request)
from flask_sqlalchemy import SQLAlchemy
from http import server
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


app = Flask(__name__)
bp = Blueprint('app', __name__)

user = 'qadeojfu' 
database = 'qadeojfu'
password = 'BXuRLcKiboerrYtUWFzh1UrwMa2kPniA' 
host = 'tuffi.db.elephantsql.com' 

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{database}' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secreta'
db = SQLAlchemy(app)

#MODELO
class Pacientes(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name_ = db.Column(db.String(60), nullable = False)
    idade = db.Column(db.String(2), nullable = False)
    estado = db.Column(db.String(2), nullable = False)
    sexo = db.Column(db.String(1), nullable = False)
    dose = db.Column(db.String(1), nullable = False)

    def __init__(self, name_, idade, estado, sexo, dose):
        self.name_ = name_
        self.idade = idade
        self.estado = estado
        self.sexo = sexo
        self.dose = dose
    
    @staticmethod
    def read_all():
        return Pacientes.query.order_by(Pacientes.idade).all()
    
    @staticmethod
    def read_single(pacientes_id):
        return Pacientes.query.get(pacientes_id)

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



@app.route('/', methods = ('GET', 'POST'))
def index():
    nome_cliente = None
    if request.method =='POST':
        form = request.form
        send_email(form['nome'], form['email'], form['phone'])
        nome_cliente = form['nome']
    return render_template('index.html', nome_cliente = nome_cliente)

if __name__ == '__main__':
    app.run(debug=True)