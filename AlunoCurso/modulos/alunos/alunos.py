from flask import Blueprint, render_template, request, redirect, flash
from models import Aluno
from database import db

bp_aluno = Blueprint('alunos', __name__, template_folder="templates")

@bp_aluno.route('/')
def index():
    dados = Aluno.query.all()
    return render_template('aluno.html', alunos = dados)

@bp_aluno.route('/add')
def add():
    return render_template('aluno_add.html')

@bp_aluno.route('/save', methods = ['POST'])
def save():
    nome = request.form.get('nome')
    matricula = request.form.get('matricula')

    if nome and matricula:
        bd_aluno = Aluno(nome, matricula)
        db.session.add(bd_aluno)
        db.session.commit()
        flash('Aluno salvo com sucesso!')
        return redirect('/alunos')
    else:
        flash('Preencha todos os campos!')
        return redirect('/alunos/add')