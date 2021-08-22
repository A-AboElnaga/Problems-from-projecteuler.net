def fun(summ=1000):
  
  a,b,c=1,1,(summ-2)
  while c>b and c>b :
    while a < int(summ/2):
       a_sqr =a**2
       b_sqr =b**2
       c_sqr =c**2
       if ((a_sqr+b_sqr)==c_sqr):
        print(f'{(a*a)} + {(b*b)} = {c*c} ')
        print(f'The Pythagorean triplet for which a + b + c = {summ} is[{a},{b},{c}]')
        return a,b,c
       a +=1
       c -=1
    a=1
    b +=1
    c= summ-(a+b)
try:
  a,b,c =fun()
  print(f'abc={a*b*c}')
except: print('no such numbers exist')
    
