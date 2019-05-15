import math
while True:
	a=input('Введите выражение ')
	if '+' in a:
		a=a.split('+')
		first=a[0]
		ch=int(first)
		second=a[1]
		nh=int(second)
		print(ch+nh)
	elif '*' in a:
		a=a.split('*')
		first=a[0]
		ch=int(first)
		second=a[1]
		nh=int(second)
		print(ch*nh)
	elif '/' in a:
		a=a.split('/')
		first=a[0]
		ch=int(first)
		second=a[1]
		nh=int(second)
		print(ch/nh)
	elif '-' in a:
		a=a.split('-')
		first=a[0]
		ch=int(first)
		second=a[1]
		nh=int(second)
		print(ch-nh)
			
			
			