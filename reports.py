limite_sup = 10

def listarQuestoes(conexao):# {{{
    q1(conexao)
    q2(conexao)
    q3(conexao)
    q4(conexao)
    q5(conexao)
    q6a(conexao)
    q6b(conexao)
    q7(conexao)
    q8(conexao)
    # q9(conexao)# }}}

def q1(conexao):# {{{

    print(">> Questão 1:")
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
        print("\nNumber os tuples:", len(resultado), "\n")

    except Exception as e:
        print ("Questão 1 falhou man: ", e)# }}}
def q2(conexao):# {{{

    print(">> Questão 2:")
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
        print("\nNumber os tuples:", len(resultado), "\n")

    except Exception as e:
        print ("Questão 2 falhou man: ", e)# }}}
def q3(conexao):# {{{

    print(">> Questão 3:")
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
        print("\nNumber os tuples:", len(resultado), "\n")

    except Exception as e:
        print ("Questão 3 falhou man: ", e)# }}}
def q4(conexao):# {{{

    print(">> Questão 4:")
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
        print("\nNumber os tuples:", len(resultado), "\n")

    except Exception as e:
        print ("Questão 4 falhou man: ", e)# }}}
def q5(conexao):# {{{

    print(">> Questão 5:")
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
        print("\nNumber os tuples:", len(resultado), "\n")

    except Exception as e:
        print ("Questão 5 falhou man: ", e)# }}}
def q6a(conexao):# {{{

    print(">> Questão 6a:")
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
        print("\nNumber os tuples:", len(resultado), "\n")

    except Exception as e:
        print ("Questão 6a falhou man: ", e)# }}}
def q6b(conexao):# {{{

    print(">> Questão 6b:")
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
        print("\nNumber os tuples:", len(resultado), "\n")

    except Exception as e:
        print ("Questão 6b falhou man: ", e)# }}}
def q7(conexao):# {{{

    print(">> Questão 7:")
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
        print("\nNumber os tuples:", len(resultado), "\n")

    except Exception as e:
        print ("Questão 7 falhou man: ", e)# }}}
def q8(conexao):# {{{

    print(">> Questão 8:")
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
        print("\nNumber os tuples:", len(resultado), "\n")

    except Exception as e:
        print ("Questão 8 falhou man: ", e)# }}}
def q9(conexao):# {{{

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
