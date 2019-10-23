import psycopg2
from reports import listarQuestoes
from crud import *

HOST = "localhost"
DB = "empresa"
USER = "postgres"
PASSWORD = "123"

limite_sup = 10

def conectarBanco():# {{{
    try:
        conn = psycopg2.connect(host=HOST, database=DB, user=USER, password=PASSWORD)
        return conn
    except Exception as e:
        print ("Não foi possível conectar ao banco de dados.")
        print ("Deu ruim manin: ", e)
# }}}
def main():# {{{

    try:
        conexao = conectarBanco()

        while True:

            q_flag = input("Deseja listar as questões? (S/n)")

            if q_flag.capitalize() == "S":
                listarQuestoes(conexao)

            i_flag = input("Deseja inserir dados em alguma tabela?(S/n)")

            if i_flag.capitalize() == "S":
                table = input("Insira tabela: ", end='')
                values = input("Insira a nova tupla abaixo:")
                # print("A: ", values, "++")
                inserirTabela(conexao,table, values)

            r_flag = input("Deseja remover dados de uma tabela?(S/n)")

            if r_flag.capitalize() == "S":
                table = input("Insira tabela: ", end='')
                condition = input("Insira a condição de remoção: ", end='')
                removerTabela(conexao,table, condition)

            l_flag = input("Deseja listar uma tabela?(S/n)")

            if l_flag.capitalize() == "S":
                table = input("Insira tabela: ", end='')
                listarTabela(conexao,table)
            quit = input("Deseja sair? (S/n)")

            if quit.capitalize() == "S":
                break

    finally:
        if(conexao): conexao.close()
# }}}

main()
