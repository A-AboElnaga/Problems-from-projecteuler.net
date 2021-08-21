import math
import time

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

def get_prime_list(n, primelist=[2]):
       '''enter (n) an intger and returns list of all primes whose index smaller than this number'''
      
       count,num =1,3
       while count < n:
            if is_prime(num) == True:
                count +=1
                primelist.append(num)
            num +=2
       return (primelist)

num=600851475143
primelist= get_prime_list(2000) #I have limited my testing to the 2000th prime(=17389) which more than enough, but this method is not that efficient a better one is Sieve of Eratosthenes algorithm 
factors=[]
for prime in primelist:
    if num % prime == 0:
        factors.append(prime)
print(factors)



#Sieve of Eratosthenes algorithm 
def primefactors(n):
   #even number divisible
   while n % 2 == 0:
      print (2),
      n = n / 2
    
   #n became odd
   for i in range(3,int(math.sqrt(n))+1,2):
     
      while (n % i == 0):
         print (i)
         n = n / i
   if n > 2:
      print (n)
 
n = 600851475143
primefactors(n)


                 

    
