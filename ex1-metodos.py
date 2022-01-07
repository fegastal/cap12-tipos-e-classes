class Racional:
    def cria_frac(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

if __name__ == '__main__':
    frac_1 = Racional()
    frac_1.cria_frac(3, 5)
    print(frac_1.numerador)
    print(frac_1.denominador)

