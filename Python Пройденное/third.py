import math
a=int(input("Введите число"))
calc=int(input("""Выберите действие
	1-тангенс
	2-косинус"""))
if calc==1:
	p=math.tan(a)
elif calc==2:
	p=math.cos(a)
print(p)