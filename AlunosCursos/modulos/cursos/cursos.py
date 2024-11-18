from flask import Blueprint, render_template, request, redirect, flash
from models import Curso, Aluno
from database import db

bp_curso = Blueprint('cursos', __name__, template_folder="templates")

@bp_curso.route('/')
def index():
    dados = Curso.query.all()
    return render_template('curso.html', cursos = dados)
    
@bp_curso.route('/add')
def add():
    a = Aluno.query.all()
    return render_template('curso_add.html', alunos = a)

@bp_curso.route('/save', methods=['POST'])
def save():
    nome = request.form.get('nome')
    dosagem = request.form.get('dosagem')
    id_paciente = request.form.get('id_paciente')
    if nome and dosagem and id_paciente:
        bd_projeto = Curso(nome, dosagem, id_paciente)
        db.session.add(bd_projeto)
        db.session.commit()
        flash('Projeto salvo com sucesso!!!')
        return redirect('/cursos')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/cursos/add')

@bp_curso.route("/remove/<int:id>")
def remove(id):
    dados = Curso.query.get(id)
    if id > 0:
        db.session.delete(dados)
        db.session.commit()
        flash('Medicamento removido com sucesso!')
        return redirect("/cursos")
    else:
        flash("Caminho incorreto!")
        return redirect("/cursos")

@bp_curso.route("/edita/<int:id>")
def edita(id):
    curso = Curso.query.get(id)
    paciente = Aluno.query.all()
    return render_template("medicamento_edita.html", dados=curso, paciente=paciente)

@bp_curso.route("/editasave", methods=['POST'])
def editasave():
    id = request.form.get('id')
    nome = request.form.get('nome')
    dosagem = request.form.get('dosagem')
    id_paciente = request.form.get('id_paciente')
    if id and nome and dosagem and id_paciente:
        curso = Curso.query.get(id)
        curso.nome = nome
        curso.dosagem = dosagem
        curso.id_paciente = id_paciente
        db.session.commit()
        flash('Dados atualizados com sucesso!')
        return redirect('/cursos')
    else:
        flash('Dados incompletos.')
        return redirect("/cursos")