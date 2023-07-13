from ler_xls import read_xls_file

def hashtable(columns):
  hash_table = {}
  for row in columns:
      for col in row:
          hash_table[col] = row[0]
  return hash_table
        
columns = read_xls_file()

dicionario_cidades = hashtable(columns)

cidade_nome = input("Digite o nome da cidade:")
#print(read_xls_file())
if cidade_nome in dicionario_cidades:
  print("CÓD:==>>",dicionario_cidades[cidade_nome])
else:
  print("Cidade não encontrada")
