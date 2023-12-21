import math
from fractions import Fraction

def FindFactors(a,b,c):
    divnum = a*c
    for num in range(1,500):
        div1 = divnum/num
        div2 = divnum/div1
        if div1+div2 == b: return int(div1), int(div2)
        if -div1-div2 == b: return -int(div1), -int(div2)

#Numbers: 16(a), 8(b), 1(c)
        
def aNot1(a,b,c,factors):
    b1 = factors[0]; b2 = factors[1]

    #16x^2 + 4x(b1) + 4x(b2) + 1

    gcf1 = math.gcd(a, b1)
    gcf2 = math.gcd(b2, c)

    factor1 = int(a/gcf1), int(b1/gcf1)
    factor2 = int(b2/gcf2), int(c/gcf2)

    returnFacts = f"({factor1[0]}x + {factor1[1]}), ({factor2[0]}x + {factor2[1]})"

    x1 = str(Fraction(factor1[1]/factor1[0]))
    x2 = str(Fraction(factor2[1]/factor2[0]))
    print(returnFacts)
    if x1 == x2:
        print(f"x = {x1}")
    else:
        print(f"x = {x1}, {x2}")

    input("Continue? ")    
    Main()


def aIs1(a,b,c,factors):
    print(f"(x - {factors[0]}), (x - {factors[1]})")
    if factors[0] == factors[1]:
        print(f"x = {factors[0]}")
    else:
        print(f"x = {factors[0]}, {factors[1]}")

    input("Continue? ")
    Main()

def Main():
    a_inp = input("a: ") or 1
    b_inp = input("b: ") or 1
    c_inp = input("c: ") or 1
    a = int(a_inp)
    b = int(b_inp)
    c = int(c_inp)
    factors = FindFactors(a,b,c)
    if not factors: print("Prime"); exit()
    if a != 1: 
        aNot1(a,b,c,factors)
    else:
        aIs1(a,b,c,factors)

Main()