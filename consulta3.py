#importar o conector
import mysql.connector
#estabelecer a conexao
conexao = mysql.connector.connect(
    host="localhost", user="root",
    password="", database="deposito")
#criar o cursor
cursor = conexao.cursor()

#solicita digitação do item a localizar
item = input("Qual item deseja localizar? ")

#executar a consulta
cursor.execute(f'''SELECT * FROM itens
WHERE descricao LIKE "%{item}%"; ''')

#exibir os dados do cursor
for linha in cursor:
    print("código   :", linha[0])
    print("descrição:", linha[1])
    print("posição  :", linha[2])
    print("-------------------")
    
#processa todos os registros do cursor
cursor.fetchall()
#retorna qts itens afetados no último comando
print(cursor.rowcount, "itens encontrados.")

#fechar a conexao
cursor.close()
conexao.close()