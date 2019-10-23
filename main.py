import psycopg2

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
        print ("Deu ruim manin: ", e)# }}}

def q1():# {{{

    print(">> Questão 1:\n")
    sql_entry = """ select *
                    from empregado
                    where endereco ilike '%Center'
                    and sexo = 'M' and left(sobrenome,1) = 'S'
                    order by nome;
                """
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
        print ("Questão 1 falhou man: ", e)# }}}

def q2():# {{{

    print(">> Questão 2:\n")
    sql_entry = """ select codigo, descricao
					from projeto
					where departamento = 5 and local = 'Natal'
					order by descricao;
                """
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
        print ("Questão 2 falhou man: ", e)# }}}

def q3():# {{{

    print(">> Questão 3:\n")
    sql_entry = """ select d.nome, local.nome
					from local, departamento d
					where d.codigo = local.departamento;
                """
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
        print ("Questão 3 falhou man: ", e)# }}}

def q4():# {{{

    print(">> Questão 4:\n")
    sql_entry = """ select nome
					from empregado
					group by nome
					having min(sexo) != max(sexo)
					order by nome;
                """
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
        print ("Questão 4 falhou man: ", e)# }}}

def q5():# {{{

    print(">> Questão 5:\n")
    sql_entry = """ select
					concat(emp.nome, ' ', emp.nomedomeio, '. ',emp.sobrenome) as name,
					date_part('year',age(emp.dtnascimento)) as anos
					from empregado as emp
					where emp.sexo = 'F'
					union
					select dep.nome as name, date_part('year',age(dep.dtnascimento)) as anos
					from dependente as dep
					where dep.sexo = 'F'
				        and date_part('year',age(dep.dtnascimento)) > 16
					order by anos desc;
                """
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
        print ("Questão 5 falhou man: ", e)# }}}

def q6a():# {{{

    print(">> Questão 6a:\n")
    sql_entry = """ select round(avg(num_dependentes.dependentes),2) as media
					from
					(select emp.codigo, count(dep.nome) as dependentes
					from empregado as emp right outer join dependente as dep
					on dep.empregado = emp.codigo
					group by emp.codigo) as num_dependentes;
                """
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
        print ("Questão 6a falhou man: ", e)# }}}

def q6b():# {{{

    print(">> Questão 6b:\n")
    sql_entry = """ select round(avg(num_dependentes.dependentes),2) as media
					from
					(select emp.codigo, count(dep.nome) as dependentes
					from empregado as emp left outer join dependente as dep
					on dep.empregado = emp.codigo
					group by emp.codigo) as num_dependentes;
                """
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
        print ("Questão 6b falhou man: ", e)# }}}

def q7():# {{{

    print(">> Questão 7:\n")
    sql_entry = """ select depa.nome
					from departamento as depa left outer join projeto as proj
					on depa.codigo = proj.departamento
					group by depa.nome
					having count(depa.nome) < 10
					order by depa.nome;
                """
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
        print ("Questão 7 falhou man: ", e)# }}}

def q8():# {{{

    print(">> Questão 8:\n")
    sql_entry = """ select
		    count(case when sexo = 'M' then sexo end) as qtdehomens,
                    count(case when sexo = 'F' then sexo end) as qtdemulheres
		    from empregado;
                """
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
        print ("Questão 8 falhou man: ", e)# }}}

def q9():# {{{

    print(">> Questão 9:\n")
    sql_entry = """ create view DADOS_PROJETO(EmpCod, EmpNome, EmpNomeDoMeio, EmpSobrenome, DepEmpCod, 						DepEmpNome, ProCod, ProDescricao, Horas,
					DepProCod, DepProNome) as select
					empr.codigo, empr.nome, empr.nomedomeio, empr.sobrenome,
					dpar1.codigo, dpar1.nome,
					proj.codigo, proj.descricao,
					trab.horas,
					dpar2.codigo, dpar2.nome
					from empregado as empr
					inner join departamento as dpar1
					on empr.departamento = dpar1.codigo
					inner join trabalhaem as trab
					on trab.empregado = empr.codigo
					inner join projeto as proj
					on trab.projeto = proj.codigo
					inner join departamento as dpar2
					on dpar2.codigo = proj.departamento
                """
    try:
        cursor = conexao.cursor()

        cursor.execute(sql_entry)
        conexao.commit()
        if (cursor.rowcount):
            print ("Registro inserido com sucesso.")

        cursor.close()

    except Exception as e:
        print ("Questão 9 falhou man: ", e)# }}}

def inserirTabela(tabela, values):# {{{

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
        print ("Deu pra inserir não bicho: ", e)# }}}

def removerTabela(tabela, condition):# {{{

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
        print ("Deu pra remover não man: ", e)# }}}

def listarTabela(tabela):# {{{

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
        print ("Deu pra listar não manin: ", e)# }}}

def listarQuestoes():# {{{
    q1()
    q2()
    q3()
    q4()
    q5()
    q6a()
    q6b()
    q7()
    q8()
    # q9()# }}}

def main():# {{{
    global conexao

    try:
        conexao = conectarBanco()

        while True:

            print("Deseja listar as questões? (S/n)")
            q_flag = input()

            if q_flag.capitalize() == "S":
                listarQuestoes()

            print("Deseja listar uma tabela?(S/n)")
            l_flag = input()

            if l_flag.capitalize() == "S":
                print("Insira tabela: ", end='')
                table = input()
                listarTabela(table)

            print("Deseja inserir dados em alguma tabela?(S/n)")
            i_flag = input()

            if i_flag.capitalize() == "S":
                print("Insira tabela: ", end='')
                table = input()
                print("Insira a nova tupla abaixo:")
                values = input()
                print("A: ", values, "++")
                inserirTabela(table, values)

            print("Deseja remover dados de uma tabela?(S/n)")
            r_flag = input()

            if r_flag.capitalize() == "S":
                print("Insira tabela: ", end='')
                table = input()
                print("Insira a condição de remoção: ", end='')
                condition = input()
                removerTabela(table, condition)

            print("Deseja sair? (S/n)")
            quit = input()

            if quit.capitalize() == "S":
                break

    finally:
        if(conexao): conexao.close()# }}}

main()
