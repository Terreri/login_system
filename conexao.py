import sqlite3
from usuario import Usuario


def cria_db():
    conn = sqlite3.connect('cadastros.db')

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE cadastros(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        sobrenome TEXT NOT NULL,
        email TEXT NOT NULL,
        celular TEXT NOT NULL,
        senha TEXT NOT NULL,
        genero TEXT NOT NULL);""")

    print("Banco e tabela criados com sucesso.")

    conn.close()


def salva_cadastro_db(user):
    conn = sqlite3.connect('cadastros.db')

    cursor = conn.cursor()

    lista = [user.nome, user.sobrenome, user.email,
             user.celular, user.senha, user.genero]

    if user.iduser:
        cursor.execute("""
            UPDATE cadastros
            SET nome = ?, sobrenome = ?, email = ?, celular = ?, senha = ?, genero = ?
            WHERE id = ?""", (user.nome, user.sobrenome, user.email, user.celular, user.senha, user.genero, user.iduser,))

    else:
        cursor.execute("""
        INSERT INTO cadastros(nome, sobrenome, email, celular, senha, genero) VALUES (?,?,?,?,?,?)""", lista)

    conn.commit()

    print('Dados salvos com sucesso')

    conn.close()


def busca_cadastros():
    conn = sqlite3.connect("cadastros.db")

    cursor = conn.cursor()

    cadastros = []

    cursor.execute("""
        SELECT id, nome, sobrenome, email, celular, senha, genero
        FROM cadastros""")

    for linha in cursor.fetchall():
        cadastros.append(
            Usuario(iduser=linha[0], nome=linha[1], sobrenome=linha[2], email=linha[3],
                    celular=linha[4], senha=linha[5], genero=linha[6])
        )

    conn.close()

    return cadastros


def verifica_email(email):
    conn = sqlite3.connect('cadastros.db')

    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, nome, sobrenome, email, celular, senha, genero
        FROM cadastros
        WHERE email = ?""", [email])

    cadastro = None

    for linha in cursor.fetchall():
        cadastro = Usuario(
            iduser=linha[0], nome=linha[1], sobrenome=linha[2], email=linha[3],
            celular=linha[4], senha=linha[5], genero=linha[6]
        )

    conn.close()

    return cadastro
