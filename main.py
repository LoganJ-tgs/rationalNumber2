from math import gcd
class Rational:

    #def getgcd(self):
    #  return gcd(self.num, self.den)
    def converttorational(self, other):
      if type(other) == int:
        return Rational(other, 1)
      elif type(other) == Rational:
        return other
      # add an error here
      else:
        raise RuntimeError("attempted to modify rational number with unsupported type")
    
    def simplify(self):
      greatestdivisor = gcd(self.num, self.den)
      self.num //= greatestdivisor
      self.den //= greatestdivisor

    def __str__(self):
      return f"{self.num}/{self.den}"
    
    def __init__(self, numer, denom):
        self.num = int(numer)
        self.den = int(denom)
        self.simplify()

    def __add__(self, other):
        other = self.converttorational(other)
        savedden = self.den
        self.num *= other.den
        self.den *= other.den
        other.num *= savedden
        other.den *= savedden
        self.num += other.num
        self.simplify()
        other.simplify()
        return self

    def __sub__(self, other):
        ther = self.converttorational(other)
        savedden = self.den
        self.num *= other.den
        self.den *= other.den
        other.num *= savedden
        other.den *= savedden
        self.num -= other.num
        self.simplify()
        other.simplify()
        return self

    def __mul__(self, other):
        other = self.converttorational(other)
        self.num *= other.num
        self.den *= other.den
        self.simplify()
        return self

    def __truediv__(self, other):
        other = self.converttorational(other)
        self *= Rational(other.den, other.num)
        self.simplify()
        return self
    #TODO: you will need to put your numerator and denominator
    #TODO: in lowest terms in multiple functions. Maybe it's a
    #TODO: good idea to make that it's own function?

def main():
    rational1 = Rational(1,2)
    rational2 = Rational(3,4)
    print(rational1*rational2)
    rational1 = Rational(1,2)
    print(rational1+rational2)
    rational1 = Rational(1,2)
    print(rational1-rational2)
    rational1 = Rational(1,2)
    print(rational1/rational2)
    print(rational1+1)


if __name__ == '__main__':
    main()
