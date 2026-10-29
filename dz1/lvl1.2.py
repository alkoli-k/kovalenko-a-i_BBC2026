def slozhenie(a, b):
    print(a + b)

def vychitanie(a, b):
    print(a - b)

def umnozhenie(a, b):
    print(a * b)

def delenie(a, b):
    if b != 0:
        print(a / b)
    else:
        print("Ошибка: деление на ноль!")

print("Введите первое число")
a = int(input())

print("Введите второе число")
b = int(input())

print("Введите знак")
c = input()

print("Ответ:")
if c == '+':
    slozhenie(a, b)
elif c == '-':
    vychitanie(a, b)
elif c == '*':
    umnozhenie(a, b)
elif c == '/':
    delenie(a, b)
else:
    print("Не знаю таких команд")
