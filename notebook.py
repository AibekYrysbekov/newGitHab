
#notebook

a = int(input("Оперативная память 4 8: "))
b = int(input('Объем диска ГБ: '))
c = int(input('Вид диска 1-SSD(256gb) 2-HDD(1T): '))
d = int(input('Цена: '))
e = int(input('Cсостояние 1-новый, 2-БУ'))
if 4 <= a <= 8 and 256 <= b and d <= 1000 and c == 1 and e == 1:
    print('есть такой ноут')
elif 4 <= a <= 8 and b <= 1000 and d <= 1000 and c == 2 and e == 1:
    print('ноут  найден')

else:
    print('ноут не найден')