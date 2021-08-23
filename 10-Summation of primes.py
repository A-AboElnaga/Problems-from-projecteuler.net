import math
import time
start= time.time()
def is_prime(num, primelist=[2, 3]):
       '''enter (num) an intger larger than or equal to 2 and returns True if prime, and False if not'''
       d= 5
       if num == 2 or num ==3:
         return (True)
       if num % 2 == 0:
         return(False)
       if num % 3 == 0:
         return(False)
       else:
         while d <= ((int(math.sqrt(num)))+1):#All primes greater than 3 can be written in the form 6k+/-1.
          if num % d == 0: #testing for 6k-1 which is 'd'
            return(False)
          elif num % (d+2)==0:  # testing for 6k+1 which is d+2
            return(False)
          else:
             d += 6     #increase k by 1 which is equivalent to d+6
       return True
summ= 2
for i in range(3,100000,2):
  if is_prime(i)== True:
    summ +=i
end= time.time()
print(summ,(end-start))
