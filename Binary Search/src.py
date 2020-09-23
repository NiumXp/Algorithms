elemento = 7
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def binary_search(array, key, start=0, end=None):
    if end == None:
        end = len(vetor)

    index = start + end // 2

    item = vetor[index]
    if item == chave:
        return index

    if start != end:
        if item < key:
            return binary_search(array, key, start + 1, end)
        else:
            return binary_search(array, key, start, end - 1)

resultado = binary_search(lista, elemento)
print(resultado)
