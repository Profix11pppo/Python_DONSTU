import math

print('hello world')
c=100+100
print(c,' рублей ')
a=input("Введите текст ")
print(a)
b=int(input("Введите число "))
print(c+b)
number=int(input("Введите число "))
number2=int(input("Введите число "))
if number2>number:
	print(' 2 число больше первого ')
elif number>number2:
	print(' 1 число больше второго')
else:
	print(' Числа равны')	

vvod=int(input())
m=math.sin(vvod)
print(m)
l=math.cos(vvod)	
print(l)
chislo=4
ml=math.sqrt(chislo)
print(ml)

calc=input("""Выберите что вы хотите сделать?
1- Сложить
2- Отнять
3- Умножить
4- Разделить	
 """)
if calc==1:
	a=int(input("Введите первое число "))
	b=int(input("Введите второе число "))
	c=a+b
	print(c)
elif calc==2:
z=3
while True:
	z=z+1
	print(z)
	if z==10:
		break
		