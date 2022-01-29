# -*- coding: utf-8 -*-
def  pr4h():
    a=input("Введите строку:")
    b=a.find("h")
    c=a.rfind("h")
    print(a[c:b:-1]+"h")
print (pr4h())