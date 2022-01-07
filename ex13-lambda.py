from pilha import Stack

def calcula_pos(exp):
    pilha_op = Stack()
    tokens = exp.split()
    for token in tokens:
        if token.isdigit():
            pilha_op.push(int(token))
        else:
            operando_2 = pilha_op.pop()
            operando_1 = pilha_op.pop()
            resultado = calcula(token, operando_1, operando_2)
            pilha_op.push(resultado)
    return pilha_op.pop()

def calcula(op, opera_1, opera_2):
    operations = ['*': lambda x, y: x * y, '+':lambda x, y: x + y, '-': lambda x, y: x- y, '//': lambda x, y: x // y}
    return operations[op] (opera_1, opera_2)
