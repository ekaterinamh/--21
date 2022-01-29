# -- coding: utf-8 --

def pr5():
  N = 0
  while N < 2:
    print ('Введите число')
    N = int(input())
  print('')
  i = 2
  while N%i != 0:
    i += 1
  
  return(i)

print(pr5())