## CONECTAR AO BANCO DE DADOS ###################
import mysql.connector
conexao = mysql.connector.connect(
    host="localhost", user="root",
    password="", database="livraria")
cursor = conexao.cursor()
#print("Conexao OK")

## FUNÇÃO CADASTRO ##############################
def cadastrar():
    print("== CADASTRO DE LIVRO ==")
    titulo = input("Título do livro: ")
    autor = input("Autor do livro: ")
    preco = input("Preço do livro: ")
    cmd="INSERT INTO livros VALUES(null, %s, %s, %s)"
    cursor.execute(cmd, (titulo,autor,preco) )
    conexao.commit()
    input("Inserido com sucesso! \n\n")

## FUNÇÃO LISTAR #################################
def listar():
    print("== LISTAGEM DE LIVROS ==")
    cursor.execute("SELECT * FROM livros")
    for linha in cursor:
        print("Código:", linha[0])
        print("Título:", linha[1])
        print("Autor:", linha[2])
        print("Preço:", linha[3])
        print("---------------------------")

## FUNÇÃO PESQUISAR ############################
def pesquisar():
    print("== PESQUISA DE LIVROS == ")
    titulo = input("Título do Livro: ")
    autor = input("Autor do Livro: ")
    cmd = f'''SELECT * FROM livros
            WHERE titulo LIKE '%{titulo}%'
            AND autor LIKE '%{autor}%' '''
    cursor.execute(cmd)
    for linha in cursor:
        print("Código:", linha[0])
        print("Título:", linha[1])
        print("Autor:", linha[2])
        print("Preço:", linha[3])
        print("---------------------------")

## FUNÇÃO ALTERAR ##############################
def alterar():
    print("== ALTERAR DADOS DO LIVRO ==")
    codigo = input("Código do livro: ")
    cursor.execute(
    "SELECT * FROM livros WHERE codigo = " + codigo)
    dados = cursor.fetchall() #converte pra lista
    if len(dados) == 0:
        print("Código não encontrado. \n")
    else:
        print("== Dados do livro ==")
        print("titulo:", dados[0][1])
        print("autor:", dados[0][2])
        print("preco:", dados[0][3])
        print("----------------------------")
        coluna = input("Qual coluna deseja alterar? ")
        valor = input(f"Qual o novo {coluna}? ")
        cursor.execute(f'''UPDATE livros
                    SET {coluna} = '{valor}'
                    WHERE codigo = {codigo}''')
        conexao.commit()
        print("Alterado com sucesso. \n\n")
        
## MENU PRINCIPAL ##############################
while True:
    print("==== MENU DO SISTEMA ====")
    print("1. Cadastrar")
    print("2. Listar")
    print("3. Pesquisar")
    print("4. Alterar")
    print("5. Sair")
    opcao = input("Opção: ")
    
    if opcao == '1':
        cadastrar()
    elif opcao == '2':
        listar()
    elif opcao == '3':
        pesquisar()
    elif opcao == '4':
        alterar()
    elif opcao == '5':
        print("Até a próxima!")
        break

