import pymongo

#criando conexão com o DB
conexao = pymongo.MongoClient()
#Criando um objeto
db = conexao.cadastrodb
#criando uma coleção
'''db.create_collection("colecao")'''
#Inserindo um documento
db.colecao.insert_one({
   'titulo': 'MongoDB com Python', 
   'descricao': 'MongoDB é um Banco de Dados NoSQL',
   'by': 'Data Science Academy',
   'url': 'http://www.datascienceacademy.com.br',
   'tags': ['mongodb', 'database', 'NoSQL'],
   'likes': 100
})

print(db.colecao.find_one(),end='\n')
col = db["colecao"]
manip = col.find_one()
for y,x in enumerate(manip.items()):
    print(f'Chave {y}: {x[0]}\nValor {y}: {x[1]}',end="\n--------------------------\n")
print(db.list_collection_names())