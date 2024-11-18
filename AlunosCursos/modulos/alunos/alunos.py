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
        id_aluno = Aluno(nome, matricula)
        db.session.add(id_aluno)
        db.session.commit()
        flash('Aluno salvo com sucesso!')
        return redirect('/alunos')
    else:
        flash('Preencha todos os campos!')
        return redirect('/alunos/add')
    
@bp_aluno.route("/remove/<int:id>")
def remove(id):
    dados = Aluno.query.get(id)
    if id > 0:
        db.session.delete(dados)
        db.session.commit()
        flash('Aluno removido com sucesso!')
        return redirect("/alunos")
    else:
        flash("Caminho incorreto!")
        return redirect("/alunos")

@bp_aluno.route("/edita/<int:id>")
def edita(id):
    aluno = Aluno.query.get(id)
    return render_template("aluno_edita.html", dados=aluno)

@bp_aluno.route("/editasave", methods=['POST'])
def editasave():
    id = request.form.get('id')
    nome = request.form.get('nome')
    matricula = request.form.get('matricula')
    if id and nome and matricula:
        aluno = Aluno.query.get(id)
        aluno.nome = nome
        aluno.matricula = matricula
        db.session.commit()
        flash('Dados atualizados com sucesso!')
        return redirect('/alunos')
    else:
        flash('Dados incompletos.')
        return redirect("/alunos")