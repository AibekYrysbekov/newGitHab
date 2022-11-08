# summa

n = int('4729461084')
s = 0
while n != 0:
    a = n % 10
    s = s + a
    n = n // 10
print(s)


'''
dates_of_birth = {3, 10, 11, 13, 31, 21, 1, 10, 3, 5, 6, 6}
dates_of_birth.remove(6)
print(dates_of_birth)
'''
'''

name = {'qwe', 'ghkhg', 'qwt', '{khd}'}
g = ['gdv', '{a,d, c}']
print(type(g))
name.update(g)
print(name)

'''

'''
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
a = farm_1.difference(farm_2)
print(a)
'''