import math


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

#prints the required prime but I commented it out and made another block with list to store the primes
# count,num =1,3
# while count < 10001:
#  if is_prime(num) == True:
#    count +=1
#  num +=2
# num -=2
# print (num)


primelist=[2]
count,num =1,3
n =10001
while count < n:
  if is_prime(num) == True:
      count +=1
      primelist.append(num)
  num +=2

print(primelist[n-1])
  
    
      
      
       
