# -- coding: utf-8 --
def strok():
	s=str(input('Введите строку: '))
	a=len(s)//2+len(s)%2
	b=(s[a:]+s[:a])
	return b
	
print('Итог:',strok())