#Escreva um programa Python para obter uma lista, classificada em ordem crescente pelo último elemento em cada tupla de uma determinada lista de tuplas não vazias.
def last(n): return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)

print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
