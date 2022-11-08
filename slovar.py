#1
'''
menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
menu['drink'] = 'cola', 'fanta', 'sprite'
print(menu, sep="\n")
'''

#2
'''
a = {}
c = 0

while c < 3:
    log = input("Введите логин: ")
    p = input('Введите пароль: ')
    a[log] = p
    c += 1
    a.update()
    print(a)
'''

#3
'''

a ={ 'Aibek': 'buhgalter',
     'Shamil': 'neftyannik',
     'Baiel': ' pilot',
     'Adahan': ' haker',
     'Rustam': 'st.haker'}
for k, v in a.items():
    print(f"Здравствуйте {k} прекрасная профессия {v}")
'''


