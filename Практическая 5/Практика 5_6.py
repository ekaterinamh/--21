# -*- coding: utf-8 -*-
def pr6():
    k=0
    x=1
    z=0
    while (x!=0):   
        x=int(input("Введите число:"))
        k=k+1
        z=z+x
    print(z/(k-1))
print (pr6())