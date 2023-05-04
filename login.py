from conexao import verifica_email
from usuario import Usuario


def verifica_login(email, senha):
    cadastro = verifica_email(email)
    if cadastro:
        if senha == cadastro.senha:
            return True
        else:
            return False
    else:
        return None


def login1(email, senha):

    verif = verifica_login(email, senha)

    if verif == True:
        print('Bem vindo')
        return 1
    elif verif == False:
        print('Senha incorreta!')
        return 2
    else:
        print('Não há cadastros com esse email')
