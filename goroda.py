data = {'city' : []}
while True:
	choice = int(input('Выберите действие: Добавить город(1), Отобразить список городов(2), Заменить город(3), Удалить город(4), Выход(5): '))
	if choice == 1:
		print('Новый город')
		city = input('Введите название города: ')
		if city not in data['city']:
			data['city'].append(city)
			print('Город добавлен!')
		else:
			print('Такой город уже есть')
	if choice == 2:
		print('Отобразить список городов')
		print(data)
	if choice == 3:
		print('Заменить город')
		actual_city = input('Введите название текущего города: ')
		new_city = input('Введите название нового города: ')
		if actual_city in data['city']:
			data['city'].remove(city)
			data['city'].append(new_city)
			print('Город заменен')
			if actual_city not in data['city']:
				print('Такой город отсутствует')
			elif new_city in data['city']:
				print(f'Такой город уже есть: {city}')
		else:
			print('Некорректное название')
	if choice == 4:
		print('Удалить город')
		name_city = input('Введите название города: ')
		if name_city in data['city']:
			data['city'].remove(city)
			print('Город удален')
		elif name_city not in data['city']:
			print('Такой город отсутствует')
		else:
			print('Некорректное название')
	if choice == 5:
		print('До свидания')
		break