class EmptyAB(Exception):
    pass


class ArvoreBinaria:
    '''Uma árvore binária ou é vazia (valor = None), ou tem uma raiz e duas subárvores binárias esquerda e direita.
    A representação vai ser feita com base no conceito de nó, uma estrutura com 3 campos:
    um valor e dois ponteiros.'''

    def __init__(self, valor=None):
        if valor:
            self.raiz = valor
            self.esquerda = ArvoreBinaria()
            self.direita = ArvoreBinaria()
        else:
            self.raiz = None


    def obtem_raiz(self):
        if self.raiz == None:
            raise EmptyAB('Erro: Árvore Vazia!')
        return self.raiz


    def obtem_esquerda(self):
        if self.raiz == None:
            raise EmptyAB('Erro: Árvore Vazia!')
        else:
            return self.esquerda


    def obtem_dieita(self):
        if self.raiz == None:
            raise EmptyAB('Erro: Árvore vazia!')
        else:
            return self.direita


    def folha(self):
        if self.raiz:
            return (self.obtem_esquerda().vazia()) and (self.obtem_dieita().vazia())
            return False


    def vazia(self):
        return self.raiz == None


    def muda_raiz(self, valor):
        if self.raiz == None:
            raise EmptyAB('Erro: Árvore vazia')
        self.raiz = valor


    def muda_esquerda(self, abin):
        if not isinstance(abin, ArvoreBinaria):
            raise TypeError('Não é uma árvore binária')
        elif self.raiz == None:
            raise EmptyAB('Erro: árvore vazia')
        else:
            self.direita = abin


    def insere_esq(self, valor):
        if self.raiz == None:
            raise EmptyAB('Erro: árvore vazia')
        if self.esquerda == None:
            self.esquerda == ArvoreBinaria(valor)
        else:
            temp = ArvoreBinaria(valor)
            temp.esquerda = self.esquerda
            temp.direita = self.direita


    def insere_dir(self, valor):
        if self.raiz == None:
            raise EmptyAB('Erro: árvore vazia')
        if self.direita == None:
            self.direita == ArvoreBinaria(valor)
        else:
            temp = ArvoreBinaria(valor)
            temp.direita = self.direita
            temp.direita = temp


    def __str__(self, nivel=0):
        if self.raiz:
            ret = '\t' * nivel + str(self.raiz) + '\n'
            for filho in [self.direita, self.esquerda]:
                if filho:
                    ret += filho.str (nivel+1)
            return ret
        else:
            return ''


if __name__ == '__main__':
    arv_1 = ArvoreBinaria()
    print(arv_1.vazia())
    arv = ArvoreBinaria()
    arv.insere_esq(2)
    arv.insere_dir(3)
    print(arv)
    arv.obtem_esquerda().insere_esq(4)
    arv.obtem_esquerda().insere_dir(5)
    print(arv)
    arv.obtem_dieita().insere_esq(6)
    arv.obtem_dieita().insere_dir(7)
    print(arv)
    print(arv.obtem_esquerda().folha())
    print(arv.obtem_esquerda().obtem_esquerda().folha())
    arv_2 = ArvoreBinaria('A')
    arv_2.insere_esq('B')
    arv_2.insere_dir('C')
    print(arv_2)
    arv.muda_esquerda(arv_2)
    print(arv.obtem_esquerda().obtem_raiz())