import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='xxx',
    database='dbyoutube'
)

cursor = conexao.cursor()

#CRUD
# comando = ''
# cursor.execute(comando)
# conexao.commit() #edta o banco de dados
#resultado = cursor.fetchall() #ler o banco de dados

#CREATE

# nome_produto = "chocolate"
# valor = 15
# comando = f'INSERT INTO tbl_vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
# cursor.execute(comando)
# conexao.commit() #edita o banco de dados

#READ

# comando = f'SELECT * FROM dbyoutube.tbl_vendas'
# cursor.execute(comando)
# resultado = cursor.fetchall() #ler o banco de dados
# print(resultado)

#UPDATE

# idProduto = 1
# valor = 6
# comando = f'UPDATE tbl_vendas SET valor = {valor} WHERE idVendas = "{idProduto}"'
# cursor.execute(comando)
# conexao.commit() #edita o banco de dados

#DELETE

idProduto = 1
comando = f'DELETE FROM tbl_vendas WHERE idVendas = "{idProduto}"'
cursor.execute(comando)
conexao.commit() #edita o banco de dados

cursor.close()
conexao.close()