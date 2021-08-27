#Method 1 Recursive Solution with Memoization
def count_paths(x,y,memo):
  length = 1
  cord=str(x)+','+str(y)
  if x==0 or y==0:
    return length
  elif cord in memo:
    length = memo[cord]
    return length 
  else:
      length= count_paths(x-1,y,memo)+count_paths(x,y-1,memo)
      memo[cord]=length
      return length
   

memo={'1,1':2,'2,2':6}
print(count_paths(20,20,memo))
end = time.time()
print(end-start)

#Method 2 Using Combinatorial Solution: (x+y)!/[x!*y!]
import math

start = time.time()

x,y=20,20
fac_y=math.factorial(y)
fac_x=math.factorial(x)
fac_x_y= math.factorial(x+y)
result= fac_x_y //(fac_x*fac_y)
print(result)
end = time.time()
print(end-start)

