from flask import Flask, render_template, request
from cadastro import *
from login import *

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    nome = request.form['firstname']
    sobrenome = request.form['lastname']
    email = request.form['email']
    celular = request.form['number']
    senha = request.form['password']
    confsenha = request.form['confpassword']
    genero = request.form['gender']

    cadastro = novo_cadastro(nome, sobrenome, email,
                             celular, senha, confsenha, genero)

    if cadastro == 2:
        use_alternate_style2 = True
        return render_template("index.html", use_alternate_style2=use_alternate_style2)
    elif cadastro == 1:
        use_alternate_style = True
        senhas_diferentes = 'Senhas não conferem'
        return render_template('index.html', use_alternate_style=use_alternate_style, senhas_diferentes=senhas_diferentes)
    elif cadastro == 3:
        return render_template("login.html")


@app.route('/logins', methods=['GET', 'POST'])
def loginst():
    email = request.form['email']
    senha = request.form['password']

    logins = login1(email, senha)

    if logins == 1:
        return render_template("main.html")

    elif logins == 2:
        use_alternate_style = True
        return render_template("login.html", use_alternate_style=use_alternate_style)
    elif logins == 3:
        use_alternate_style2 = True
        return render_template("login.html", use_alternate_style2=use_alternate_style2)


if __name__ == '__main__':
    app.run(debug=True)
