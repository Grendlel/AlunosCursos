from database import db

class Aluno(db.Model):
    __tablename__ = 'aluno'
    id_aluno = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    matricula = db.Column(db.String(50))

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __repr__(self):
        return "<Aluno: {}>".format(self.nome)
    
class Curso(db.Model):
    __tablename__ = 'Curso'
    id_curso = db.Column(db.Integer, primary_key = True)
    aluno_id = db.Column(db.Integer, db.ForeignKey('aluno.id_aluno'))
    nome = db.Column(db.String(100))
    duracao = db.Column(db.String(50))

    aluno = db.relationship('Aluno', foreign_keys=aluno_id)

    def __init__(self, aluno_id, nome, duracao):
        self.aluno_id = aluno_id
        self.nome = nome
        self.duracao = duracao

    def __repr__(self):
        return "<Curso do Aluno: {} - {} - {}>".format(self.aluno.nome, self.nome, self.duracao)
        