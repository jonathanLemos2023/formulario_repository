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
print("Conexão bem sucedida")




comando_dql = "SELECT * FROM dbo.Tabela_Pessoa"

cursor = conexao.cursor()



dados = pd.read_sql(comando_dql, conexao)


#nome = "jonathan"
#empresa = "kraftone"

#Values
#({numero},'{nome}','{empresa}')

comando_inserir = """INSERT INTO [dbo].[Tabela_Pessoa]
           ([Num_Pessoa]
           ,[Nome_Pessoa]
           ,[Nome_Empresa]
           ,[Email]
           ,[Telefone_Celular]
           ,[Telefone_Fixo]
           ,[Funcao]
           ,[Observacoes])
VALUES
    (2,'jonathan','KRAFTONE','jonathan@email.com','1111111111','2222222222','testador','nenhuma observação')"""

cursor.execute(comando_inserir)
cursor.commit()

print(dados)

