import math
import time

#This method takes around 11 seconds on my machine
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
for i in range(3,2000000,2):
  if is_prime(i)== True:
    summ +=i
end= time.time()
print(summ,'Time taken using prime testing :',(end-start))




#Using Sieve of Eratosthenes algorthim for a more effiecient soultion
#This method takes less than 1 second on my machine
start= time.time()
def SieveOfEratosthenes(n):
    # Create a list of boolean values where the index represents the value of the number "prime[0..n]"     
    # and initialize all entries as true. A value in prime[i] will
    #finally be false if i is Not a prime, else true.
    
    prime = [True for i in range(n+1)]
    for i in range(4, n + 1, 2):
                prime[i] = False
    list1=[]
    p = 3
    while (p * p <= n):
         
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
             
            # Update all multiples of p
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False # '0' is not a prime so set index 0 to False
    prime[1]= False # '1' is not a prime so set index 1 to False
    # Return list of all prime numbers smaller than n
    for p in range(n + 1):
        if prime[p]:
             list1.append(p) 
    return list1
# driver program
if __name__=='__main__':
    n = 2000000
    
    summ=0
    for prime in SieveOfEratosthenes(n):
      summ += prime
    end= time.time()
    print (summ,'Time taken using Sieve of Eratosthenes :',(end-start))
