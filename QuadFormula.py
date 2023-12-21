import math
def GetSign(num: float):
    if num >=0: return "+"
    if num <0: return ""
a_inp = input("a: ") or 1
b_inp = input("b: ") or 1
c_inp = input("c: ") or 1
a = int(a_inp)
b = int(b_inp)
c = int(c_inp)
#Quad form(case a): (-b +- sqrt(pow(b,2)-(4*a*b)))/2

Solution_plus = (-b + math.sqrt(pow(b,2)-(4*a*c)))/(2*a)
Solution_mins = (-b - math.sqrt(pow(b,2)-(4*a*c)))/(2*a)
if Solution_plus == Solution_mins:
    print(f"x = {Solution_plus}")
else:
    print(f"x = {Solution_plus}, {Solution_mins}")