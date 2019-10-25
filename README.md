## Dependencias
python 3.5+
pip install psycopg2

Além disto é necessário que exista um banco postgres de nome 'empresa',
conforme o arquivo prova.sql, com usuario 'postgres' e senha 'postgres'.

## Executar
```
python3 main.py
```

### Como Utilizar
Ao executar o programa lhe será oferecida as opções padrões de *CRUD*, ou seja,
o usuário terá as opções de: (1) **inserir novos dados em alguma tabela**, (2)
**listar as informações existentes de alguma tabela**, (3) **atualizar dados
de alguma tabela**, e (4) **remover dados de alguma tabela**. Além destas
operações, o usuário também pode escolher (5) **ver análises pré-definidas
do banco de dados**.

Vale ressaltar a importância de prestar atenção às tipagens corretas
dos atributos de cada tabela, ou seja, se você quer adicionar um novo **NOME**
(claramente uma string), utilize as aspas simples na digitação no terminal.

A opção de sair do programa também será informada, e o usuário poderá fazê-la
a qualquer momento, contanto que não esteja no meio de outra operação.

#### ATENÇÃO

É necessário que o usuário tenha conhecimento das relações de antemão. Deverá
saber os nomes tanto das tabelas quanto dos atributos de cada tabela, e deverá
saber quais atributos devem ser vistos como ***string*** e quais não, pois
tais atributos devem ser digitados entre aspas simples.

Exemplo de como passar as informações de uma inserção à tabela *DEPARTAMENTO*:

'<Nome_Desejado>' <Número_de_Código> '<CPF_de_Funcionário>'
'<Data_de_Nascimento>'

Nota-se que somente o segundo campo encontra-se sem aspas, pois este é um
campo que requer um inteiro.
