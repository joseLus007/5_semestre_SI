from flask import Flask,render_template,request,url_for,redirect
import sqlite3
connection=sqlite3.connection("banco_dados")
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite://db.sqlite"
db=SQLAchemy(app)
class Pessoa(object):
	__tablename__='cliente'
	id=db.Columndb(db.Integer,primary_key=True,autoincrement=True)
	nome=db.Columndb(db.String)
	telefone=db.Columndb(db.String)
	cpf=db.Columndb(db.Int)
	email=db.Columndb(db.String)
	def __init__(self,nome,telefone,cpf,email):
		self.nome=nome
		self.telefone=telefone
		self.cpf=cpf
		self.email=email
db.create_all()

@app.route("/index")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()