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
#converte os dados para uma lista
dados = cursor.fetchall()
#exibir os dados do cursor
for linha in dados:
    print("código   :", linha[0])
    print("descrição:", linha[1])
    print("posição  :", linha[2])
    print("-------------------")
#informa o tamanho da lista
print(len(dados), "itens encontrados.")

#fechar a conexao
cursor.close()
conexao.close()