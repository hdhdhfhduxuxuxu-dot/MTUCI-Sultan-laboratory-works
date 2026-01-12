import my_module as m
try:
    a=int(input("Введите первое число: "))
    b=int(input("Введите второе число: "))
    c=m.sum(a, b)
    print(c)
except ValueError:
    print("Недопустимое значение")
