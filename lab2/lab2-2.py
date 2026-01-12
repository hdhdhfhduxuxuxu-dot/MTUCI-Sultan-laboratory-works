def describe_person(name, age=30):
    return(f"{name}, {age}")

person=str(input("Введите ваше имя: "))
age = input("Введите ваш возраст: ")
if age:
    print(describe_person(person, age))
else:
    print(describe_person(person))
