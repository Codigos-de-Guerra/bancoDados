## Dependencias 
python 3.5+
pip install psycopg2

Além disto é necessário que exista um banco postgres de nome 'empresa' conforme o arquivo prova.sql, com usuario 'postgres' e senha '123'

## Executar
```
python3 main.py
```

## Utilização
Ao executar o programa lhe será perguntado se deseja: (1) **listar as queries da prova**, (2) **inserir novos dados em alguma tabela**, (3) **remover dados em alguma tabela** e, por último, (4) **listar as informações existentes de alguma tabela**. As perguntas serão sequenciais e estarão cometendo um crime contra a leitura e usabilidade do usuário, mas como programador deste projeto não aguenta mais fica assim mesmo. Vale ressaltar que as informações passadas ao programa devem coincindir com as informações presentes no **banco**, ou seja, passe uma tabela que exista. Nos campos de inserção, deve-se prestar atenção às tipagens também, ou seja, se você quer adicionar um novo **NOME** (claramente uma string), utilize as aspas simples na digitação no terminal.

Ao final das 4 operações, será perguntado se deseja sair da execução ou não. Caso deseje continuar, as mesmas perguntas, em sequência, irão ocorrer novamente até que o usuário decida parar a execução.
