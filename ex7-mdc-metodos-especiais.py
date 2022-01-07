def mdc(m,n):
    if m % n == 0:
        return n
    else:
        return mdc(n, m % n)


class Racional:
    def __init__(self, numerador, denominador):
        g = mdc(numerador, denominador)
        self.numerador = numerador
        self.denominador = denominador


    def __str__(self):
        if self.denominador == 1:
            return "%d" % self.numerador
        else:
            return "%d / %d" % (self.numerador, self.denominador)


    def __mul__(self, outro):
        if isinstance(outro, int):
            outro = Racional(outro)
        novo_numerador = self.numerador * outro.numerador
        novo_denominador = self.denominador * outro.denominador
        return Racional(novo_numerador, novo_denominador)

    __rmul__ = __mul__


    def __add__(self, outro):
        if isinstance(outro, int):
            outro = Racional(outro)
        novo_numerador = self.numerador * outro.denominador + self.denominador * outro.numerador
        return Racional(novo_numerador, novo_denominador)

    __radd__ = __add__


if __name__ == '__main__':
    frac_1 = Racional(12, -8)
    frac_2 = Racional(4, 3)
    print(frac_1)
    printt(frac_2)
    frac_3 = frac_1 * frac_2
    frac_4 = frac_1 * 2
    frac_5 = 2 + frac_1
    print(frac_3)
    print(frac_4)
    print(frac_5)

