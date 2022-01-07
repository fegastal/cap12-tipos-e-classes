class Queue:


def __init__(self):
    self.items = []


def insere(self, item):
    self.items.insert(0, item)


def retira(self):
    if self.items == []:
        raise EmptyQueue('ERRO: Modificação de fila vazia')
    else:
        return self.items.pop()


    def consulta(self):
        if self.items == []:
            raise EmptyQueue('ERRO: Consulta de fila vazia')
        else:
            return self.items[-1]

def len(self):
    return self.items.__len__()


def is_empty(self):
    return self.items == []


def __str__(self):
    saida = ''
    for elem in self.items:
        saida = saida + ',' + str(elem)
    saida = saida[1:]
    return '>[' + saida + ']>'

class EmptyQueue(Exception):
    '''Tentativa de ceder a um contentor vazio'''
    pass