def size(pilha):
    aux = deepcopy(pilha)
    if aux.is_empty():
        return 0
    else:
        aux.pop()
        return 1 + size(aux)