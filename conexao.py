import mysql.connector
conexao = mysql.connector.connect(
    host="localhost", user="root",
    password="", database="estante")
cursor = conexao.cursor()
#######################################
cursor.execute(
    '''INSERT INTO livros VALUES(null,
    'Inglês Moderno','Steve Dee')''')
conexao.commit()
print("Inserido com sucesso")