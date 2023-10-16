from flask import Flask, render_template, request, redirect, url_for
import pyodbc
import pandas as pd


dados_conexao = (
    "Driver={SQL Server};"
    "Server=NOTEBOOK-LENOVO;"
    "Username=Kratone;"
    "Password=2023;"
    "Database=DB_Vendas;"
)

conexao = pyodbc.connect(dados_conexao)

comando_dql = "SELECT * FROM Tabela_Pessoa"
dados = pd.read_sql(comando_dql, conexao)

cursor = conexao.cursor()



app = Flask(__name__)


@app.route('/')
def home():

    return render_template('home.html')


@app.route('/tabela_pessoa')
def tabela_pessoa():

    cursor.execute('SELECT * FROM Tabela_Pessoa')

    column_names = [desc[0] for desc in cursor.description]

    data = cursor.fetchall()

    return render_template('tabela_pessoa.html', data=data, column_names=column_names)


@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    mensagem = None
    if request.method == 'POST':
        Numero_pessoa = request.form['Numero_pessoa']
        Nome_pessoa = request.form['Nome_pessoa']
        Nome_empresa = request.form['Nome_empresa']
        email = request.form['email']
        Telefone_celular = request.form['Telefone_celular']
        Telefone_fixo = request.form['Telefone_fixo']
        funcao = request.form['funcao']
        observacoes = request.form['observacoes']

        cursor.execute("SELECT * FROM Tabela_Cliente WHERE Nome_Empresa = ?", Nome_empresa)
        empresa_existente = cursor.fetchone()

        if empresa_existente:

            comando_inserir = f"""INSERT INTO [dbo].[Tabela_Pessoa]
                       ([Num_Pessoa]
                       ,[Nome_Pessoa]
                       ,[Nome_Empresa]
                       ,[Email]
                       ,[Telefone_Celular]
                       ,[Telefone_Fixo]
                       ,[Funcao]
                       ,[Observacoes])
            VALUES
                ({Numero_pessoa},'{Nome_pessoa}','{Nome_empresa}','{email}',
                '{Telefone_celular}','{Telefone_fixo}','{funcao}','{observacoes}')"""

            cursor.execute(comando_inserir)
            cursor.commit()

            mensagem = 'Dados adicionados com sucesso!!'

        else:
            mensagem = 'Esta empresa não existe no banco de dados. Insira um nome de Empresa valída!'


    return render_template('formulario.html', mensagem = mensagem)

if __name__ == '__main__':
    app.run(debug=True)