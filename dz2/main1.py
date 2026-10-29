def lvl_1(method, text):
    if method == "upper":
        return text.upper()
    elif method == "lower":
        return text.lower()
    elif method == "capitalize":
        return text.capitalize()
    else:
        return "Неизвестный метод"
        
def lvl_2(method, text):
    if method == "find":
        print('Напишите слово, индекс которого хотите найти')
        wrd = input()
        return text.find(wrd)
    elif method == "replace":
        print('Напишите слово, которое хотите заменить')
        wrd1 = input()
        print('Напишите слово для замены')
        wrd2 = input()
        return text.replace(wrd1, wrd2)
    elif method == "count":
        print('Напишите слово или строку, количество которых хотите посчитать')
        wrd = input()
        return text.count(wrd)
    else:
        return "Неизвестный метод"
        
def lvl_3(method, text):
    if method == "split":
        print("Напишите символ, по которому делится строка")
        sym1 = input()
        print("Напишите символ, на который заменить предыдущий символ")
        sym2 = input()
        return sym2.join(text.split(sym1))
    elif method == "join":
        print("Напишите символ, по которому делятся элементы списка")
        sym = input()
        return sym.join(text.split(','))
    else:
        return "Неизвестный метод"
        
def lvl_4(method, text):
    if method == "isdigit":
        return text.isdigit()
    elif method == "isalpha":
        return text.isalpha()
    elif method == "strip":
        print("Напишите символы, которые хотите удалить (или нажмите Enter для удаления пробелов)")
        sym = input()
        if sym == "":
            return text.strip()
        return text.strip(sym)
    else:
        return "Неизвестный метод"

while True:
    print("\nВыберите уровень (1, 2, 3, 4, 5) или 0 для выхода:")
    lvl = int(input())
    
    if lvl == 0:
        print("Выход из программы.")
        break
        
    if lvl == 1:
        test = "пРиВет МИР"
        print("Метод upper: пРиВет МИР ->", test.upper())
        print("Метод lower: пРиВет МИР ->", test.lower())
        print("Метод capitalize: пРиВет МИР ->", test.capitalize())
        print("Выберите метод: upper, lower, capitalize")
        method = input()
        print("Напишите свой текст:")
        text = input()
        print("Результат:", lvl_1(method, text))
        
    elif lvl == 2:
        test = "Ботать это круто. Очень круто"
        print(f"Тестовая строка - {test}")
        print("Метод find (ищем индекс первого вхождения слова 'круто') ->", test.find("круто"))
        print("Метод replace (замена слова 'круто' на 'не круто') ->", test.replace("круто", "не круто"))
        print("Метод count (считаем количество букв 'о') ->", test.count("о"))
        print("Выберите метод: find, replace, count")
        method = input()
        print("Напишите свой текст:")
        text = input()
        print("Результат:", lvl_2(method, text))
        
    elif lvl == 3:
        test = "1,2,3,4"
        print(f"Текстовая строка - {test}")
        print("Метод split (делим строку по запятым) ->", test.split(","))
        print("Метод split+join (разделяем строку пробелами) ->", " ".join(test.split(",")))
        print("Метод join (разделяем список символами '!') ->", '!'.join(test.split(",")))
        print("Выберите метод: split, join")
        method = input()
        print("Напишите свой текст:")
        text = input()
        print("Результат:", lvl_3(method, text))
        
    elif lvl == 4:
        test1 = "1234"
        test2 = "   abc   "
        print(f"Текстовые строки - '{test1}' и '{test2}'")
        print("Метод isdigit (все ли цифры):", test1.isdigit(), test2.isdigit())
        print("Метод isalpha (все ли буквы):", test1.isalpha(), test2.isalpha())
        print("Метод strip (убирает пробелы по краям):", f"'{test2.strip()}'")
        print("Выберите метод: isdigit, isalpha, strip")
        method = input()
        print("Напишите свой текст:")
        text = input()
        print("Результат:", lvl_4(method, text))  
        
    elif lvl == 5:
        test = '       pYtHon;is;AWESome;       '
        print(f"Исходная строка: '{test}'")
        test = test.strip()
        test = " ".join(test.split(";"))
        test = test.lower()
        print("Результат обработки уровня 5:", test.capitalize())
