'''Uma pilha é uma coleção ordenada de objetos em que os últimos elementos a serem inseridos são também
os primeiros a serem retirados. Função append acrescenta elementos e pop elimina / devolve elementos.'''


class Stack:

    def __init__(self):
        self.Stack = []

    def push(self,object):
        self.Stack.append(object)

    def pop(self):
        if self.is_empty():
            raise ValueError
        return self.stack.pop()

    def top(self):
        if self.is_empty():
            raise ValueError
        else:
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0