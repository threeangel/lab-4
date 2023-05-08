def z1():
    try:
        number = int(input("введи число: "))
    except ValueError:
        print("где цифры")
    else:
        if number % 3 == 0:
            print("делится на 3")
        elif number == 0:
            print("какой 0")
        else:
            print("не делится на 3")

def z2():
    try:
        n = int(input("введи число: "))
        v = 100 / n
    except ValueError:
        print("где цифры")
    except ZeroDivisionError:
        print("какой 0")
    else:
        print("100 / ", n, " = ", v)

def z3():
    d = input("введи дату: ")
    d = d.split(".")
    if int(d[0]) * int(d[1]) == int(d[2][2 : 4]):
        print("ты волшебник?")
    else:
        print("ты не волшебник!")

def z4():
    ch = input("введи номер билета: ")
    x = 0
    y = 0
    if len(ch) % 2 == 0:
        for i in ch[0:int(len(ch) / 2)]:
            x = x + int(i)
        for i in ch[int(len(ch) / 2):int(len(ch)) + 1]:
            y = y + int(i)
        if x == y:
            print("ю ар со лаки")
        else:
            print("ю ар со анлаки")
    else:
        print("номерок не подходит")