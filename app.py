from flask import Flask, render_template, request, redirect, flash
from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.curso_dao import CursoDAO

app = Flask(__name__)
app.secret_key = "chave_secreta_e_muito_longa"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/aluno') 
def listar_aluno(): 
    dao = AlunoDAO() 
    aluno = dao.listar()
    return render_template('aluno/listar_aluno.html', lista=aluno)

@app.route('/aluno/form')
def form_aluno():
    return render_template('aluno/form.html', aluno=None)

@app.route('/aluno/salvar/', methods=['POST'])
def aluno_salvar():
    nome = request.form['nome']
    idade = request.form['idade']
    cidade = request.form['cidade']
    dao = AlunoDAO()
    result = dao.salvar(nome, idade, cidade)

    if result["status"] == "ok":
        flash("Registro salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")

    return redirect('/aluno')

@app.route('/professor') 
def listar_professor(): 
    dao = ProfessorDAO() 
    professor = dao.listar()
    return render_template('professor/listar_professor.html', lista=professor)


@app.route('/professor/form')
def form_professor():
    return render_template('professor/form.html', professor=None)

@app.route('/professor/salvar/', methods=['POST'])
def professor_salvar():
    nome = request.form['nome']
    disciplina = request.form['disciplina']
    dao = ProfessorDAO()
    result = dao.salvar(nome, disciplina)

    if result["status"] == "ok":
        flash("Registro salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")

    return redirect('/professor')

@app.route('/curso') 
def listar_curso(): 
    dao = CursoDAO() 
    curso = dao.listar()
    return render_template('curso/listar_curso.html', lista=curso)

@app.route('/curso/form')
def form_curso():
    return render_template('curso/form.html', curso=None)

@app.route('/curso/salvar/', methods=['POST'])
def curso_salvar():
    nome_curso = request.form['nome_curso']
    duracao = request.form['duracao']
    dao = CursoDAO()
    result = dao.salvar(nome_curso, duracao)

    if result["status"] == "ok":
        flash("Registro salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")

    return redirect('/curso')

@app.route('/saudacao')
def saudacao():
    return render_template('saudacao/saudacao.html')

@app.route('/saudacao1/<nome>')
def saudacao1(nome):
    return render_template('saudacao/saudacao.html', valor=nome)

@app.route('/saudacao2/')
def saudacao2():
    nome = request.args.get('nome')
    return render_template('saudacao/saudacao.html', valor=nome)

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    senha = request.form['senha']
    data = f"Usuário: {usuario} | Senha: {senha}"
    return render_template('saudacao/saudacao.html', valor=data)

@app.route('/desafio')
def desafio():
    return render_template('desafio/desafio.html')

@app.route('/registro', methods=['POST'])
def registro():
    nome = request.form['nome']
    dataNasc = request.form['dataNasc']
    cpf = request.form['cpf']
    nome_mae = request.form['nome_mae']
    valor = f"Nome: {nome} | Data Nascimento: {dataNasc} | CPF: {cpf} | Noma da Mãe: {nome_mae}"
    return render_template('desafio/desafio.html', valor=valor)

if __name__ == "__main__":
    app.run(debug=True)