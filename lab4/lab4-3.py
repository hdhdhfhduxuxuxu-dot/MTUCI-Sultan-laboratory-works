from package import numbers as n
from package import strokes as s

#числа

try:
    a=int(input("Введите первое число: "))
    b=int(input("Введите второе число: "))
    ans=int(input("Введите число от 1 до 4: 1-сумма, 2-разность, 3-умножение, 4-деление: "))
    if ans==1:
        print(n.sum(a, b))
    elif ans==2:
        print(n.dif(a, b))
    elif ans==3:
        print(n.mult(a, b))
    elif ans==4:
        print(n.div(a, b))
    else:
        print("Недопустимое значение")
except ValueError:
    print("Недопустимое значение")

#строки

try:
    c=str(input("Введите текст: "))
    ans=int(input("Введите число от 1 до 2: 1-длина текста, 2-перевернуть текст: "))
    if ans==1:
        print(s.lenght(c))
    elif ans==2:
        print(s.reverse(c))
    else:
        print("Недопустимое значение")
except ValueError:
    print("Недопустимое значение")
