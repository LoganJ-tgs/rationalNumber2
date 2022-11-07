from math import gcd
class Rational:

    #def getgcd(self):
    #  return gcd(self.num, self.den)
    def converttorational(self, other):
      if type(other) == int:
        return Rational(other, 1)
      elif type(other) == Rational:
        return other.makeclone()
      # add an error here
      else:
        raise RuntimeError("attempted to modify rational number with unsupported type")

    def makeclone(self):
      return Rational(self.num, self.den)
      
    def simplify(self):
      greatestdivisor = gcd(self.num, self.den)
      self.num //= greatestdivisor
      self.den //= greatestdivisor

    def __float__(self):
      return self.num / self.den
    
    def __str__(self):
      return f"{self.num}/{self.den}"
    
    def __init__(self, numer, denom):
        self.num = int(numer)
        self.den = int(denom)
        self.simplify()

    def __add__(self, other):
        other = self.converttorational(other)
        newden = self.den * other.den
        selfnumnew = self.num * other.den
        othernumnew = other.num * self.den
        return Rational(selfnumnew + othernumnew, newden)

    def __sub__(self, other):
        other = self.converttorational(other)
        newden = self.den * other.den
        selfnumnew = self.num * other.den
        othernumnew = other.num * self.den
        return Rational(selfnumnew - othernumnew, newden)

    def __mul__(self, other):
        other = self.converttorational(other)
        newrational = Rational(self.num * other.num, self.den * other.den)
        newrational.simplify()
        return newrational

    def __truediv__(self, other):
        other = self.converttorational(other)
        newrational = self * Rational(other.den, other.num)
        newrational.simplify()
        return newrational


    def __radd__(self, other):
      return self.makeclone() + other

    def __rsub__(self, other):
      return Rational(other, 1) - self

    def __rmul__(self, other):
      return self.makeclone() * other

    def __rtruediv__(self, other):
      return Rational(other, 1) / self
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
    rational1 = Rational(1,2)
    print(rational1+1)
    rational1 = Rational(1,2)
    print(1+rational1)
    print(1-rational1)
    print(1*rational1)
    print(1/rational1)


def testthing():
  a = Rational(1,2)
  b = 2
  print(type(b))
  c = a - b
  print(type(b))
  print(a - b)
  print(a+ b)
  print(a*b)
  print(a/b)
    

  


if __name__ == '__main__':
    #main()
    testthing()
