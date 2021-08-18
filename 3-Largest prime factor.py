import math
def get_prime_list(num, primelist=[2,3,5,7,11]):
    '''enter (num) an intger and returns list of all prime smaller than this number'''
   
    for i in range(primelist[-1]+1,num):
        stat=[]
        for prime in primelist:
            if i % prime == 0:
                stat.append(False)
            else:
                stat.append(True)
        if False not in stat:
                primelist.append(i)
    return (primelist)
num=600851475143 
primelist= get_prime_list(10000) #I have limited my testing but this method is not that efficient a better one is Sieve of Eratosthenes algorithm 
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


                 

    
