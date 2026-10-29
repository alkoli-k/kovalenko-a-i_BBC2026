def aa(n1, n2, op):
    if op == '+':
        print(n1 + n2)
    elif op == '-':
        print(n1 - n2)
    elif op == '*':
        print(n1 * n2)
    elif op == '/':
        if n2 == 0:
            print("Ошибка: деление на ноль!")
        else:
            print(n1 / n2)
    else:
        print("Не знаю таких команд")

while True:
    print("Введите первое число")
    a = float(input())
    print("Введите второе число")
    b = float(input())
    print("Введите знак")
    c = input()
    aa(a, b, c)
    print("---")
