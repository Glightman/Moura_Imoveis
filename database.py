from flask_sqlalchemy import SQLAlchemy
import app

user = 'qadeojfu' 
database = 'qadeojfu'
password = 'BXuRLcKiboerrYtUWFzh1UrwMa2kPniA' 
host = 'tuffi.db.elephantsql.com' 

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
    estado_propriedade_id = db.Column(db.Integer, db.ForeignKey('prop_state.id'))
    space_id = db.Column(db.Integer, db.ForeignKey('space.id'))
    banheiro = db.Column(db.Integer, nullable = False)
    quarto = db.Column(db.Integer, nullable = False)
    cidade = db.Column(db.String(25), nullable = False)
    views = db.Column(db.Integer, nullable = False)
    data_cadastro = db.Column(db.DateTime, nullable = False)

    def __init__(self, user_id, status_id, category_id, estado_propriedade_id, space_id, banheiro, quarto, cidade, views, data_cadastro):
        self.user_id = user_id
        self.status_id = status_id
        self.category_id = category_id
        self.estado_propriedade_id = estado_propriedade_id
        self.space_id = space_id
        self.banheiro = banheiro
        self.quarto = quarto
        self.cidade = cidade
        self.views = views
        self.data_cadastro = data_cadastro

#MODELO DAS CATEGORIAS
class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    category_name = db.Column(db.String(60), nullable = False)

#MODELO DOS ESPAÇOS
class Space(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    space_name = db.Column(db.String(60), nullable = False) 

#MODELO DO ESTADO DA PROPRIEDADE
class Prop_state(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    prop_state_name = db.Column(db.String(60), nullable = False)

#MODELO DE STATUS DO IMÓVEL
class Status(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    status_name = db.Column(db.String(60), nullable = False)

#MODELO DAS FOTOS DOS IMOVEIS
class Image(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    image = db.Column(db.LargeBinary, nullable = False)
    imovel_id = db.Column(db.Integer, db.ForeignKey('imovel.id'))

#MODELO DAS FOTOS DO USUÁRIO
class User_img(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_img = db.Column(db.LargeBinary, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


    @staticmethod
    def read_all():
        return User.query.order_by(User.idade).all()
    
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