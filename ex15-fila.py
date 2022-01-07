def batata_quente(lista_nomes, n):
    fila = Queue()

    #Constrói fila de nomes
    for nome in lista_nomes:
        fila.insere(nome)

    #Simula Jogo
    while fila.len() > 1:
        print(fila)
        for i in range(n):
            fila.insere(fila.retira())
        fila.retira()
    return fila.consulta()