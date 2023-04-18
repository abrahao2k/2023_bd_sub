#importar o conector
import mysql.connector
#estabelecer a conexao
conexao = mysql.connector.connect(
    host="localhost", user="root",
    password="", database="deposito")
#criar o cursor
cursor = conexao.cursor()

#executar a consulta
cursor.execute("SELECT * FROM itens")

#exibir os dados do cursor
for linha in cursor:
    print("código   :", linha[0])
    print("descrição:", linha[1])
    print("posição  :", linha[2])
    print("-------------------")