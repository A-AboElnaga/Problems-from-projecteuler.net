import math


def factors(num):
  factors_list=[1,]
  for x in range(2,int(math.sqrt(num))+1):
    if num%x ==0:
      factors_list.append(x)
      if x != num//x:
        factors_list.append(num//x)
  return factors_list 


def sum_factors(num):
  summ=0
  for factor in factors(num):
    summ+=factor
  return summ


def is_num_abundant (num):
  
  if sum_factors(num) > num:
    return True
  else: return False
    

abundants = set(i for i in range(1,28124) if sum_factors(i) > i)
def abundantsum(i):
        return any(i-a in abundants for a in abundants)

print (sum(i for i in range(1,28124) if not abundantsum(i)))  
  
  
