import math

from ler_xls import read_xls_file

def jump_search(arr, target, cidade_cod):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while arr[min(step, n)-1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    while arr[prev] < target:
        prev += 1

        if prev == min(step, n):
            return -1

    if arr[prev] == target:
        return cidade_cod[arr[prev]]

    return -1
 
data = read_xls_file()

def hashtable(columns):
  hash_table = {}
  for row in columns:
      for col in row:
          hash_table[col] = row[0]
  return hash_table

cidades_sorted = sorted([data[i][1] for i in range(len(data))])

cidade = input("Digite o nome da cidade: ")

codigo = jump_search(cidades_sorted, cidade, hashtable(data))

if codigo == -1:
  print("Cidade não encontrada")
else:
  print(f"Código da cidade {cidade}: {codigo}")
