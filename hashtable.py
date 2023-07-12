from ler_xls import read_xls_file

def hashtable(columns):
  hash_table = {}
  for row in columns:
      for col in row:
          hash_table[col] = row[0]
  return hash_table
        
columns = read_xls_file()

result = hashtable(columns)

print(result['Brasília'])