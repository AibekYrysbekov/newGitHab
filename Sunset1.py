# Задание №1
'''
print("Ноль в качестве знака операции"   
      "\nзавершит работу программы")
while True:
    s = input("Знак (+,-,*,/): ")
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            print("%.2f" % (x+y))
        elif s == '-':
            print("%.2f" % (x-y))
        elif s == '*':
            print("%.2f" % (x*y))
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")

'''

# Задание № 2

'''
while True:
    a = int(input("Введите число: "))
    b = int(input("Введите число: "))
    c = int(input("Введите число: "))

    num1 = a
    num2 = b
    num3 = c

    a = num1 + num2
    b = num3 - num1
    c = num1 + num2 + num3
    print(a, b, c)
'''


# Задание №3
'''
a = int(input('Введите сторону квадрата: '))
s = a**2
p = a+a+a+a
print(' Площадь квадрата = см2: ', s)
print("Периметр квадрата =: ", p)
'''
# Задание № 4
# Задание № 5
# Задание № 6