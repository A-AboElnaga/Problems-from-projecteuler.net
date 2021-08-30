import math


def factors(num):
  factors_list=[1,]
  for x in range(2,int(math.sqrt(num))+1):
    if num%x ==0:
      factors_list.append(x)
      factors_list.append(num//x)
  return factors_list 


def sum_factors(num):
  summ=0
  for factor in factors(num):
    summ+=factor
  return summ


def is_num_Amicable (num):
  
  if sum_factors(sum_factors(num))==num and sum_factors(num)!= num:
    return True
  else: return False
    
  
res=0
for x in range(2,10000):
  if is_num_Amicable(x):
    res+=x
print(res)
