from prettytable import PrettyTable

from conexao import salva_cadastro_db, busca_cadastros, verifica_email
from usuario import Usuario


# lista_contatos será usados apenas para efeito de apresentação dos metodos nesse modelo de login

def lista_cadastros():
    table = PrettyTable(["Nome", "Sobrenome", "Email",
                        "Celular", "Senha", "Genero"])

    for cadastro in busca_cadastros():
        table.add_row([cadastro.nome, cadastro.sobrenome, cadastro.email,
                       cadastro.celular, cadastro.senha, cadastro.genero])
    print(table)


def novo_cadastro(nome, sobrenome, email, celular, senha, confsenha, genero):

    cadastro = verifica_email(email)

    if senha != confsenha:
        print('Senhas não conferem')
        return 1

    if cadastro:
        print(f"O email {email} já esta cadastrado")
        return 2

    salva_cadastro_db(Usuario(nome, sobrenome, email, celular, senha, genero))

    lista_cadastros()

    return 3
