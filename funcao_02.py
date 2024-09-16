def ordena_bubble(lista):
    try:
        n = len(lista)
        for i in range(n):
            for j in range(0, n-i-1):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        return True, lista
    except Exception as e:
        print(f"Erro ao ordenar lista pelo método Bubble Sort: {e}")
        return False, None

# função insertion:
def ordena_insertion(lista):
    try:
        for i in range(1, len(lista)):
            key = lista[i]
            j = i - 1
            while j >= 0 and key < lista[j]:
                lista[j + 1] = lista[j]
                j -= 1
            lista[j + 1] = key
        return True, lista
    except Exception as e:
        print(f"Erro ao ordenar lista pelo método Insertion Sort: {e}")
        return False, None

# função selection:
def ordena_selection(lista):
    try:
        for i in range(len(lista)):
            min_idx = i
            for j in range(i+1, len(lista)):
                if lista[j] < lista[min_idx]:
                    min_idx = j
            lista[i], lista[min_idx] = lista[min_idx], lista[i]
        return True, lista
    except Exception as e:
        print(f"Erro ao ordenar lista pelo método Selection Sort: {e}")
        return False, None

# função quick:
def ordena_quick(lista):
    try:
        if len(lista) <= 1:
            return True, lista
        else:
            pivot = lista[0]
            lesser = [x for x in lista[1:] if x <= pivot]
            greater = [x for x in lista[1:] if x > pivot]
            return True, ordena_quick(lesser)[1] + [pivot] + ordena_quick(greater)[1]
    except Exception as e:
        print(f"Erro ao ordenar lista pelo método Quick Sort: {e}")
        return False, None