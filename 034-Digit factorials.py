#Built-in factorial function
import math

res=0
for x in range(3,100000):
  summ=0
  str_x = str(x)
  for char in str_x:
    summ +=math.factorial(int(char))
  if summ== x:
     res+=x
print (res)

    
#Defining our factorial function by build up from 1 to x  
    
def fact(x):
    res=1
    for num in range(1,x+1):
      res*=num
    return res
  
res=0
for x in range(3,100000):
  summ=0
  str_x = str(x)
  for char in str_x:
    summ +=fact(int(char))
  if summ== x:
     res+=x
print (res)

    
#Defining our factorial function with memo  
    
def fact(x,memo={0:1,1:1}):
  if x in memo:
    return memo[x]
  else: 
    for num in range(x,1,-1):
      memo[x]= x*fact(x-1)
  return memo[x]

res=0
for x in range(3,100000):
  summ=0
  str_x = str(x)
  for char in str_x:
    summ +=fact(int(char))
  if summ== x:
     res+=x
print (res)

    
