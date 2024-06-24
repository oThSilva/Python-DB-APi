import sqlite3
from pathlib import Path


# Para criar um database na pasta raiz
ROTH_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROTH_PATH / "clientes.sqlite")

# Para executar comandos SQL
cursor = conexao.cursor()


def criar_tabela(conexao, cursor):
    cursor.execute(
        "CREATE TABLE  clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR (100), email VARCHAR(150))"
    )
    conexao.commit()


def criar_cliente(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes(nome, email) VALUES (?,?);", data)
    conexao.commit()


def atualizar_registros(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email = ? WHERE id = ?", data)
    conexao.commit()


# atualizar_registros(conexao, cursor, "Th", "th@gmail.com", 1)


def excluir_registros(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id = ?", data)
    conexao.commit()


# excluir_registros(conexao, cursor, 1)


def inserir_muitos(conexao, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES(?,?)", dados)
    conexao.commit()


dados = [
    ("Giovanna", "Giovanna@gmail.com"),
    ("Fred", "Fred@gmail.com"),
    ("Alfredo", "Alfredo@gmail.com"),
]

# inserir_muitos(conexao, cursor, dados)


# def recuperar_clientes(cursor, id):
#     cursor.execute("SELECT * FROM clientes WHERE id = ?", (id,))
#     return cursor.fetchone()


# cliente = recuperar_clientes(cursor, 2)
# print(cliente)


# Alterando o Row_factory


def consultar_clientes(cursor, id):
    cursor.row_factory = sqlite3.Row
    cursor.execute("SELECT * FROM clientes WHERE id = ?", (id,))
    return cursor.fetchone()


cliente = consultar_clientes(cursor, 2)
print(dict(cliente))


def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes")


clientes = listar_clientes(cursor)
for cliente in clientes:
    print(dict(cliente))

try:
    cursor.execute(
        "INSERT INTO clientes (id, nome, email) VALUES (?,?,?) ",
        (2, "Teste2", "teste2@teste.com"),
    )
    conexao.commit()
except Exception as exc:
    print(f"Ops, alguma coisa deu errada! Erro: {exc}")
    conexao.rollback()
