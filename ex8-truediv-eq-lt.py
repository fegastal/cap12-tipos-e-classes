class Racional:


    def __init__(self, numerador, denominador):
        g = mdc(numerador, denominador)
        self.numerador = numerador // g
        self.denominador = denominador // g


    def __str__(self):
        if self.denominador == 1:
            return "%d" % self.numerador
        else:
            return "%d / %d" % (self.numerador, self.denominador)


    def __mul__(self, outro):
        if isinstance(outro, int):
            outro = Racional(outro)
        return Racional(self.numerador * outro.denominador + self.denominador * outro.numerador)

    __rmul__ = __mul__


    def __add__(self, outro):
        if isinstance(outro, int):
            outro = Racional(outro)
        return Racional(self.numerador * outro.denominador + self.denominador * outro.numerador, self.denominador * outro.denominador)

    __radd__ = __add__

    def __sub__(self, outro):
        return Racional(self.numerador * outro.denominador - self.denominador * outro.numerador,
        \ self.denominador * outro.denominador)


        def __truediv__(self, outro):
            return Racional(self.numerador * outro.denominador, self.denominador * outro.numerador)
        

        def __eq__(self, outro):
            if self is outro:
                return True
            elif type(self) != type(outro):
                return False
            else:
                return (self.numerador == outro.numerador) and \ (self.denominador == outro.denominador)


        def __lt__(self, outro):
            extremos = self.numerador * outro.denominador
        meios = self.denominador * outro.numerador
        return extremos < meios


    def _mcd(selfself, m, n):
        if m % n == 0:
            return n
        else:
            return self._mdc(n, m % n)


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

