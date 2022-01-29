# -*- coding: utf-8 -*-

def obuv():
	a=int(input('расстояние между рядами a='))
	b=int(input('расстояние между дырочками в ряду b='))
	l=int(input('длина свободного конца шнурка l='))
	N=int(input('количество дырочек N='))
	return 2*(a+b)* (N-1)+2*l+a
print("Длина шнурка:", obuv())