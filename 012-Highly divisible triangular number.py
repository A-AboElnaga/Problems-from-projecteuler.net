import math, time

# # method 1: by counting every triangular number's factors
# start= time.time()
# def factors(n):
#     list_of_factors=[]
#     for i in range(1,int(math.sqrt(n+1))):
#       if (n % i == 0):
#           list_of_factors.append(i)
#           if int(n/i) not in list_of_factors:
#             list_of_factors.append(int(n/i))
#     return(list_of_factors)
  
# big =1
# for k in range (2500,100000):
#   n = k*(k+1)/2
#   list_of_factors = factors(n)
#   if big < len((list_of_factors)):
#     big = len(list_of_factors)
#     big_list= list_of_factors.copy()
#   if len(list_of_factors) >= 500:
#     print (n)
#     end= time.time()
#     print(end-start)
#     break


# method 2: by calculating num of factors from num of prime factors 
#The number of divisors D(N) of any integer N can be computed from:
# D(N) = (a_1+1) ( (a_2+1) ( (a_3+1) ( ...
# a_n being the exponents of the distinct prime numbers which are factors of N
# For example, the number of divisors of 28 would thus be:
# D(28) = (2+1)*(1+1) = 3*2 = 6 

start= time.time()
def Num_of_factors(n): 
    f2=0
    ft=1
    while n % 2 == 0:
      f2 +=1
      n = n / 2
    ft *= (f2+1) 
    for i in range(3,int(math.sqrt(n))+1,2):
      fi= 0
      while (n % i == 0):
          fi += 1
          n = n / i
      ft *=(fi+1)
    if n > 2:
          ft *= 2
    return ft
  

big =1
num_of_factors_of_k =[Num_of_factors(k) for k in range (1,20000)]
for k in range (1,20000):
  if k%2 == 0:
    factors_k= num_of_factors_of_k[int((k-1)/2)]
    factors_k_1 =num_of_factors_of_k[k] 
  else: 
    factors_k= num_of_factors_of_k[k-1]
    factors_k_1 =num_of_factors_of_k[int(k/2)]
  num_of_factors =factors_k *factors_k_1
  big_num= k*(k+1)/2
  if big < num_of_factors:
    big = num_of_factors
  if num_of_factors >= 500:
    print (big_num)
    end= time.time()
    print(end-start)
    break


