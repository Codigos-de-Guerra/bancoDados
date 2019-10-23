def inserirTabela(conexao,tabela, values):# {{{

    values = values.split()
    print(values)
    buff = ""
    for val in values:
        buff += str(val) + ","
    buff = buff[:-1]

    print(buff)
    sql_entry = """ insert into {}
                    values ({});
                """.format(tabela, buff)

    try:
        cursor = conexao.cursor()

        cursor.execute(sql_entry)
        conexao.commit()
        if (cursor.rowcount):
            print ("Registro inserido com sucesso.")

        cursor.close()

    except Exception as e:
        print ("Deu pra inserir não bicho: ", e)
# }}}
def removerTabela(conexao,tabela, condition):# {{{

    print(">> Removendo da tabela: {}".format(tabela), "\n")
    sql_entry = """ delete from {}
                    where {};
                """.format(tabela, condition)
    try:
        cursor = conexao.cursor()

        # postgres_insert_query = """ DELETE FROM departamento WHERE codigo = 99"""
        cursor.execute(sql_entry)
        conexao.commit()
        if (cursor.rowcount):
            print ("Registro excluído com sucesso.")

        cursor.close()

    except Exception as e:
        print ("Deu pra remover não man: ", e)
# }}}
def listarTabela(conexao, tabela):# {{{

    print(">> Listando tabela: {}".format(tabela), "\n")
    sql_entry = """ select *
                    from {};
                """.format(tabela)
    try:
        cursor = conexao.cursor()

        cursor.execute(sql_entry)
        resultado = cursor.fetchall()
        for idx, tupla in enumerate(resultado):
            if idx > limite_sup:
                print("...\n...\n...")
                break
            buff = ""
            for attr in tupla:
                buff += str(attr) + " - "
            print(buff[:-2])

        cursor.close()
        print("\nNumber os tuples: ", len(resultado), "\n")

    except Exception as e:
        print ("Deu pra listar não manin: ", e)
# }}}
