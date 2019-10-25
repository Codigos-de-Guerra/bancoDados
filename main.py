import psycopg2
from reports import listarQuestoes
from crud import *

HOST = "localhost"
DB = "empresa"
USER = "postgres"
PASSWORD = "postgres"

def conectarBanco():# {{{
    try:
        conn = psycopg2.connect(host=HOST, database=DB, user=USER, password=PASSWORD)
        return conn
    except Exception as e:
        print ("Não foi possível conectar ao banco de dados.")
        print ("Deu ruim manin: ", e)
# }}}
def main():# {{{

    while True:
        try:
            conexao = conectarBanco()
        except:
            print("Q")
        print("Que operação deseja realizar? Insira a letra correspondente.")
        print(">>> [C]: Para adicionar dados.\n>>> [R]: Para ler dados.")
        print(">>> [U]: Para atualizar dados.\n>>> [D]: Para deletar dados.")
        print(">>> [P] Para ver os relatórios pré-definidos.")
        print(">>> [Q]: Se nenhuma operação for desejada e quiser sair.")
        buff = "---" * 20 + "\n"
        option = input(buff)

        if option.capitalize() == "C":
            table = input("Insira tabela: ")
            values = input("Insira a nova tupla abaixo:\n")
            inserirTabela(conexao,table, values)

        elif option.capitalize() == "R":
            table = input("Insira tabela: ")
            listarTabela(conexao,table)

        elif option.capitalize() == "U":
            table = input("Insira tabela: ")
            att = input("Insira a atualização desejada:\n")
            condition = input("Insira a condição de atualização: ")
            atualizarTabela(conexao, table, att, condition)

        elif option.capitalize() == "D":
            table = input("Insira tabela: ")
            condition = input("Insira a condição de remoção: ")
            removerTabela(conexao,table, condition)

        elif option.capitalize() == "P":
            listarQuestoes(conexao)

        elif option.capitalize() == "Q":
            break

        quit = input("Continuar programa? (S/N)\n")

        if quit.upper() == "N":
            break

    if(conexao): conexao.close()
# }}}

main()
