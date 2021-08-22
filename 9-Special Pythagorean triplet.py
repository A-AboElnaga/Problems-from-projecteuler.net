
def fun(summ=1000):
  counter=0
  a,b,c=1,1,(summ-2)
  while c>a and c>b :
    while a < int(summ/2) and  b> a :
       a_sqr =a**2
       b_sqr =b**2
       c_sqr =c**2
       counter+=1
       if ((a_sqr+b_sqr)==c_sqr):
        print(f'{(a*a)} + {(b*b)} = {c*c} ')
        print(f'The Pythagorean triplet for which a + b + c = {summ} is[{a},{b},{c}]')
        return a,b,c,counter
       a +=1
       c -=1
    a=1
    b +=1
    c= summ-(a+b)
  return counter
try:
  a,b,c,counter =fun()
  print(f'abc={a*b*c}')
  print(counter)
except: 
  print('no such numbers exist')
  counter= fun()
  print(counter)
