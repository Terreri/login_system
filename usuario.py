class Usuario():
    def __init__(self, nome, sobrenome, email, celular, senha, genero, iduser=None):
        self.iduser = iduser
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.celular = celular
        self.senha = senha
        self.genero = genero
