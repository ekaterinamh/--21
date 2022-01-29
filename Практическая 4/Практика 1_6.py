# -*- coding: utf-8 -*-
def pr4st():
    a=input("введите строку:")
    b=a.find("f")
    if a.find("f")==a.rfind("f") >=1:
        print("-1")
    elif a.find("f")!=a.rfind("f"):
        print(a.find("f",b+1))
    if a.find("f")==-1:
        print("-2")
    return "Конец"
print (pr4st())