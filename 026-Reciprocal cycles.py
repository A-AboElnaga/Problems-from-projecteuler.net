def Reciprocal_cycles(num):
  x = 10%num
  start= x
  counter=0
  while start!=0: 
#Primes p such that the decimal expansion of 1/p has period p-1
#which is the greatest period possible for any integer.
      if counter >num: 
        x =(x*10)%num
        start= x
        counter=0
      start= (start*10) % num
      counter+=1
      if num==1000:
        return(0)
      if start == 0:
        return(0)
      if start == x:
        return(counter)
  return(counter)
  
import time
start= time.time()

big=0
d=0
count=0
dic={}
for num in range(1,1001,1): #you can change the step to 2 and only search odd numbers because primes have the biggest factors and primes are all odd except 2
  count +=1
  length =Reciprocal_cycles(num)
  dic[num]=length
  if length > big:
    big = length
    d = num
  if count >1002:
    break
print(d,big)
end = time.time()
print(end-start)

    
