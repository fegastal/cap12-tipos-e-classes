'''

def len(self):
    return self.stack.__len__()


def __str__(self):
    saida = ''
    for elem in self.stack[::-1]:
        saida = str(elem) + ',' + saida
    saida = saida[:-1]
    return '[' + saida + ' >] '


if __name__ == '__main__':
    p_1 = Stack()
    p_1.push('A')
    p_1.push('B')
    print(p_1)

if __name__ == '__main__':
    pilha = Stack()
    pilha.push(1)
    pilha.push('abc')
    pilha.push([1, 2, 3])
    print(pilha)

'''