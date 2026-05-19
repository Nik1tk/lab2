from math import*
a=int(input("Введите кэффициент а:"))
b=int(input("Введите кэффициент b:"))
c=int(input("Введите кэффициент c:"))
if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(с, (int, float)):
        raise TypeError("Arguments must be numbers")
D=(b**2)-4*a*c
if D>0:
    x1=(-b-(sqrt(D)))/(2*a)
    x2=(-b+(sqrt(D)))/(2*a)
    print(x1,x2,(x2-x1))
if D==0:
    x=(-b)/(2*a)
    print(x)
if D<0:
    print("Корней нет")
