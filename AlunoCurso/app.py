from flask import Flask, render_template, request, flash, redirect, Blueprint
app = Flask(__name__)
app.config['SECRET_KEY'] = 'sTriMGqUENgMSAbE'
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/AlunosCursados"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from database import db
from flask_migrate import Migrate
from models import Aluno, Curso
db.init_app(app)
migrate = Migrate(app, db)

from modulos.alunos.alunos import bp_aluno
app.register_blueprint(bp_aluno, url_prefix = '/alunos')

from modulos.cursos.cursos import bp_curso
app.register_blueprint(bp_curso, url_prefix = '/cursos')

@app.route('/')
def index():
    return render_template("inicio.html")