def Reciprocal_cycles(num):
  x = 10%num
  start= x
  counter=0
  while start!=0: 

#change the counter limit to the max of your scanning limit
#Primes p such that the decimal expansion of 1/p has period p-1
#which is the greatest period possible for any integer.
# I set it to 1000 beacause my search range is for numbers less than 1000
      if counter >1000: 
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
  


big=0
d=0
count=0
dic={}
for num in range(1,1001,1):
  count +=1
  length =Reciprocal_cycles(num)
  dic[num]=length #storing the data because its cool
  if length > big:
    big = length
    d = num
  if count >1002: #You may delete this if condition but i kept it because I usually get stuck in infinite loops, so I use breaks
    break
print(d,big)


    
