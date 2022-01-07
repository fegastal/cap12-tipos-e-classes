class Racional:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        return "%d / %d" % (self.numerador, self.denominador)

if __name__ == '__main__':
    frac_1 = Racional(3,5)
    print(frac_1)

