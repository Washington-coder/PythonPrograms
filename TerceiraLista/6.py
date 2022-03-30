a = int(input())
b = int(input())
c = int(input())

if (a <= (b+c)) and (b <= (c+a)) and (c <= (a+b)):
    if (a == b) and (b == c):
        print("EQUILATERO")
    elif (a == b and a != c) or (b == c and b != a) or (c == a and c != b):
        print("ISOSCELES")
    elif a != b and a != c and b != c:
        print("ESCALENO")
else:
    print(a,b,c)