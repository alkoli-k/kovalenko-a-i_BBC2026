print("Введите первое число")
a = int(input())

print("Введите второе число")
b = int(input())

print("Введите знак")
c = input()

print("Ответ:")
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '/':
    if b != 0:
        print(a / b)
    else:
        print("Ошибка: деление на ноль!")
elif c == '*':
    print(a * b)
else:
    print("Не знаю таких команд")
