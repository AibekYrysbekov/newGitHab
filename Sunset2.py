# Задание № 1
'''
for i in range(1001):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
'''

# Задание № 2
'''
a = 333   
b = 555
num = a
a = b 
b = num
print(a)
print(b)

'''
# Задание № 3
'''
n = int('4729461084')
s = 0
while n != 0:
    a = n % 10
    s = s + a
    n = n // 10
print(s)
'''

# Задание № 4
'''
a = int(input('Введите год  в формате ГГГГ: '))
b = int(input('Введите месяц в формате -ММ: '))
c = int(input('Введите день в формате -ДД: '))
d = input('Введите время в формате ЧЧ:ММ: ')

e = {"date": a, "year": b, "month": c, "time": d}
for k, v in e.items():
   print(k, v)
   
'''
# Задание № 5
'''
a = input("Введите слово: ")
b = input("Введите слово: ")
c = input("Введите слово: ")
d = input("Введите слово: ")
e = input("Введите слово: ")
num = a + b + c + d + e
num = 5
print(num)


a = (input("Введите слово: "))
b = a * 7
b = 7
print(b)
'''

# Задание № 6

'''
pwd  
ls 
mkdir -p Work/Home_work
ls
'''

# Задание № 7

'''
Задачу не понял но решил написать два варианта ДО и ОТ.
Вход:                                   Выход
pwd                                 ls                           
ls                                  cd ../.. # прыгаем с файла сразу на два шага назад
cd Desctop                          ls 
ls                                  
cd Developer 
ls
'''