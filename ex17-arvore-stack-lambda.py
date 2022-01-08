def postorder(arvore):
    if arvore.vazia():
        return []
    elif arvore.folha():
        return [arvore.obtem_raiz()]
    else:
        return postorder(arvore.obtem_esquerda()) + postorder(arvore.obtem_direita()) + [arvore.obtem_raiz()]

def calcula_pos(exp):
    pilha_op = Stack()
    for token in exp:
        if token.isdigit():
            pilha_op.push(int(token))
        else:
            operando_2 = pilha_op.pop()
            operando_1 = pilha_op.pop()
            resultado = calcula(token, operando_1, operando_2)
            pilha_op.push(resultado)
        return pilha_op.pop()

def calcula(op, opera_1, opera_2):
    operations = {'*': lambda x, y: x * y, '+': lambda x, y: x + y, '-': lambda x, y: x - y, '//': lambda x, y: x // y}
    return operations[op] (opera_1, opera_2)


if __name__ == '__main__':
    exp_e = ArvoreBinaria('*')
    exp_e.insere_esq('5')
    exp_e.insere_dir('3')
    exp_d = ArvoreBinaria('//')
    exp_d.insere_esq('4')
    exp_d.insere_dir('2')
    exp = ArvoreBinaria('+')
    exp.muda_esquerda(exp_e)
    exp.muda_direita(exp_d)
    nova_exp = postorder(exp)
    print(nova_exp)
    print(calcula_pos(nova_exp))