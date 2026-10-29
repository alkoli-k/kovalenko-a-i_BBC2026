import random
vse_kabineti = ["пусто", "кресло с добычей", "злой ассистент", "пропуск", "бормашина", "пусто"]
karmani = []
health = 100
has_propusk = False
player_x = 0
player_y = 0
karta = []
karta_posisheniy = []
for i in range(6):
    stroka = []
    stroka_posisheniy = []
    for j in range(6):
        kabinet = random.choice(vse_kabineti)
        stroka.append(kabinet)
        stroka_posisheniy.append(False) 
    karta.append(stroka)
    karta_posisheniy.append(stroka_posisheniy)

karta[2][3] = "лифт"
karta[0][0] = "вход"
karta[5][5] = "выход"

print("ДОБРО ПОЖАЛОВАТЬ В СТОМАТОЛОГИЧЕСКИЙ ЛАБИРИНТ!")
print("Цель: найти ПРОПУСК и добежать до ВЫХОДА (в правый нижний угол).")
while health > 0:
    karta_posisheniy[player_x][player_y] = True
    print("\n=== КАРТА КЛИНИКИ ===")
    for i in range(6):
        stroka_ekrana = ""
        for j in range(6):
            if i == player_x and j == player_y:
                stroka_ekrana += "🏃 " 
            elif i == 5 and j == 5:
                stroka_ekrana += "🚪 "
            elif karta_posisheniy[i][j] == True:
                stroka_ekrana += "⬜️ "
            else:
                stroka_ekrana += "❓ "
        print(stroka_ekrana)
    print(f"\nЗдоровье ваших зубов: {health}")
    print(f"Есть пропуск?: {'ДА' if has_propusk else 'НЕТ'}")
    print(f"Что лежит в карманах: {karmani}")
    текущая_комната = karta[player_x][player_y]
    
    if текущая_комната == "злой ассистент":
        print("\n👹 На вас напал Злой Ассистент!")
        урон = random.randint(15, 30)
        health -= урон
        print(f"Он насильно осмотрел вас! Вы потеряли {урон} HP.")
        
        print("За мучения вы получили Обезболивающее!")
        karmani.append("обезболивающее")
        karta[player_x][player_y] = "пусто"  # Очищаем комнату

    elif текущая_комната == "бормашина":
        print("\n⚙️ Включилась автоматическая бормашина!")
        if "щетка" in karmani:
            print("Вы заблокировали дрель зубной щеткой! Урон снижен!")
            health -= 5
        else:
            health -= 20
            print("Вам просверлили зуб без анестезии! -20 HP.")
        karta[player_x][player_y] = "пусто"

    elif текущая_комната == "кресло с добычей":
        print("\n💺 Вы нашли стоматологическое кресло, а на столике лежала Зубная Щетка!")
        vibor = input("Положить щетку в карман? (yes/no): ").lower()
        if vibor == "yes":
            karmani.append("щетка")
            print("Щетка добавлена в карман!")
        karta[player_x][player_y] = "пусто"

    elif текущая_комната == "пропуск":
        print("\n🪪  На столе главврача лежит Электронный Пропуск!")
        vibor = input("Взять его? (yes/no): ").lower()
        if vibor == "yes":
            has_propusk = True
            karmani.append("пропуск")
            print("Вы взяли пропуск! Теперь бегите к выходу!")
        karta[player_x][player_y] = "пусто"

    elif текущая_комната == "лифт":
        print("\n🛗 Лифт закрылся и отвез вас в случайное место!")
        player_x = random.randint(0, 5)
        player_y = random.randint(0, 5)
        karta[player_x][player_y] = "пусто" 
        continue  

    elif текущая_комната == "выход":
        if has_propusk:
            print("\n🎉  Вы приложили пропуск и сбежали из клиники! ")
            break
        else:
            print("\nТурникет заперт! Бегите искать пропуск в других кабинетах!")

    print("\nЧто будете делать?")
    print("1 - вверх, 2 - вниз, 3 - влево, 4 - вправо")
    print("5 - навести порядок в карманах, 6 - сдаться")
    vibor = input("Ваш выбор: ").lower()

    if vibor == "6":
        print("Вы сдались стоматологам...")
        break

    elif vibor == "5":
        if len(karmani) == 0:
            print("В карманах пусто!")
        else:
            print(f"\nВаши вещи: {karmani}")
            print("1 - Отсортировать вещи по алфавиту")
            print("2 - Использовать обезболивающее (+30 HP)")
            print("3 - Выбросить первую вещь из кармана")
            действие = input("Выберите цифру: ")
            
            if действие == "1":
                karmani.sort()
                print("Вы разложили вещи по порядку.")
            elif действие == "2":
                if "обезболивающее" in karmani:
                    health += 30
                    karmani.remove("обезболивающее")
                    print("Вы выпили обезболивающее! Зубы больше не болят. +30 HP")
                else:
                    print("У вас нет обезболивающего!")
            elif действие == "3":
                vibrisheno = karmani.pop(0)
                print(f"Вы выбросили в урну: {vibrisheno}")

    elif vibor == "1" and player_x > 0:
        player_x -= 1
    elif vibor == "2" and player_x < 5:
        player_x += 1
    elif vibor == "3" and player_y > 0:
        player_y -= 1
    elif vibor == "4" and player_y < 5:
        player_y += 1
    else:
        print("Туда нельзя пойти, там стена!")

if health <= 0:
    print("\n ИГРА ОКОНЧЕНА! ")
    print("Здоровье зубов закончилось, и злой стоматолог поставил вам 32 пломбы!")

