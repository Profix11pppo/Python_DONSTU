import random
h=int(input("""Ты Ядровская?
		1-Поэтапно(да)
		2-Инкскейп(нет) """))
if h==1:
	print('Изучайте условие тачпада ')
elif h==2:
	k=1000
	while True:
		print("Проходите в вип зал ")
		print("У вас ",k,' рублей')
		stavka=int(input('Введите ставку '))
		kub=random.randint(1,6)
		chislo=int(input("Угадай число "))
		if kub==chislo:
			print("Вы угадали ")
			k=k+stavka
		else:
			print('Вы не угадали ')
			k=k-stavka	

