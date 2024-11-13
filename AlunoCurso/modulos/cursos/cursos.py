from flask import Blueprint, render_template, request, redirect, flash
from models import Curso, Aluno
from database import db

bp_aluno = Blueprint('cursos', __name__, template_folder="templates")

@bp_aluno.route('/')
def index():
    dados = Curso.query.all()
    return render_template('curso.html', curso = dados)

@bp_aluno.route('/add')
def add():
    a = Aluno.query.all()
    return render_template('curso_add.html', usuarios = a)

@bp_aluno.route('/save', methods = ['POST'])
def save():
    aluno_id = request.form.get('aluno_id')
    nome = request.form.get('nome')
    duracao = request.form.get('duracao')
    if aluno_id and nome and duracao:
        aluno_id = Curso(aluno_id, nome, duracao)
        db.session.add(aluno_id)
        db.session.commit()
        flash('Curso salvo com sucesso!')
        return redirect('/cursos')
    else:
        flash('Preencha todos os campos!')
        return redirect('/cursos/add')