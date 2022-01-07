def parent_equilib(exp):
    pilha = Stack()
    for ch in exp:
        if ch == '(' or ch == '[' or ch == '{':
            pilha.push(ch)
        elif ch == ')' or ch == ']' or ch == '}':
            if pilha.is_empty():
                return False
            else:
                topo = emparelhado(ch,topo):
                return False
        else:
            pass
    return pilha.is_empty()

def emparelhado(ch_1, ch_2):
    return (ch_1 == ')' and ch_2 == '(') or \
           (ch_1 == ']' and ch_2 == '[') or \
           (ch_1 == ')' and ch_2 == '{')
