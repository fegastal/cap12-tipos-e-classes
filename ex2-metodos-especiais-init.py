class Racional:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
        
if __name__ == '__main__':
    frac_1 = Racional(3,5)
    print(frac_1.numerador)
    print(frac_1.denominador)
    print(frac_1)

