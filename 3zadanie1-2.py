n = int('4729461084')
s = 0
while n != 0:
    a = n % 10
    s = s + a
    n = n // 10
print(s)