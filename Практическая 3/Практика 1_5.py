# -- coding: utf-8 --
def pr5nat():
	sum=0
	n=int(input('Введите n= '))
	for i in range(1,n+1):
		sum+=i**3
	return sum
print('Сумма равна',pr5nat())