class Racional:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        return "%d / %d" % (self.numerador, self.denominador)

    def produto(self, outro):
        novo_numerador = self.numerador * outro.numerador
        novo_denominador = self.denominador * outro.denominador
        return Racional (novo_numerador, novo_denominador)

if __name__ == '__main__':
    frac_1 = Racional(3, 5)
    frac_2 = Racional(4, 6)
    frac_3 = frac_1.produto(frac_2)
    print(frac_3)

