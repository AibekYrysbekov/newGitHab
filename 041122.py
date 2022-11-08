'''

a = int(input("вводите натуральные числа "))
m = a % 10
a = a//10
while a > 0:
    if a % 10 > m:
        m = a % 10
    a = a//10
print ('Наибольшая цифра в нем:',m)

'''


from random import random
N = 1000
q = 0
for i in range(N):
    if int(random()*100) % 2 == 0:
        q += 1
print("%.2f%%" % (q / N * 100))