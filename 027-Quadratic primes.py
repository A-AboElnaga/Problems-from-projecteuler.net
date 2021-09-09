import math
import time 

start = time.time()
def is_prime(num, primelist=[2, 3]):
       '''enter (num) an intger larger than or equal to 2 and returns True if prime, and False if not'''
       d= 3
       if num == 2:
         return (True)
       if num % 2 == 0:
         return(False)
       while d <= ((int(math.sqrt(num)))+1):
         if num % d == 0 :
          return(False)
         else:
           d += 2
       return True
       
def primes(n):
  primelist=[2]
  count,num =1,3
  while count < n:
    if is_prime(num) == True:
        count +=1
        primelist.append(num)
    num +=2
  return primelist
  
  
primelist=primes(168)
prime_counter= 0       
big =1

for a in range(-999,1001,2):
  for b in primelist:
    if (a+b+1) in primelist:
      prime_counter= 0
      for n in range(0,100):
        num = (n**2)+ (a*n)+ (b)
        if num in primelist:
            prime_counter +=1
        else: break
      
    if big < prime_counter:
      big = prime_counter
      a_best= a
      b_best=b

end= time.time()
print(f' a = {a_best}, b = {b_best}, ab = {a_best*b_best}')
print(end-start)
