# 1.Объединить 2 множества
# months_a = set(["Jan", "Feb", "March", "Apr", "May", "June"])
# months_b = set(["July", "Aug", "Sep", "Oct", "Nov"])
# 2.Добавить месяц, которого нету во множестве
# 3.Перебрать элементы множества
# 4.Вам даны 2 множества, узнать какие элементы пересекаются между ними.
# x = {1, 2, 3}
# y = {4, 3, 6}

months_a = set(["Jan", "Feb", "March", "Apr", "May", "June"])
months_b = set(["July", "Aug", "Sep", "Oct", "Nov"])
months_a.update(months_b)
months_a.update(["Dec"])
print(months_a)
for i in months_a:
    print(i)

x = {1, 2, 3}
y = {4, 3, 6}

x.intersection_update(y)
print(x)
