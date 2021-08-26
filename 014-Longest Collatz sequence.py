import time


#Method 1:Brute Force

# start= time.time()
# big =1

# for num  in range (1,1000001):
#   ori= num
#   Collatz_sequence =[] 
#   while num> 1:
#     if num%2 == 0:
#       num //= 2
#     else:
#       num = (3*num )+1
#     Collatz_sequence.append(num)
#     if len(Collatz_sequence) > big:
#       big =len(Collatz_sequence)
#       res = ori
#       seq= Collatz_sequence.copy()
# end= time.time()
# print(end-start)


#Method 2:Recursive soultion using Memoization (more efficient)

start = time.time()
def Collatz(num,memo):
  ori = num
  if num in memo:
    return memo[num]
  else:
    length=0
    while num> 1:
        if num%2 == 0:
          num //= 2
          length +=1
        else:
          num = ((3*num )+1)//2
          length +=2
        if num in memo:
          length += memo[num]
          num=1
    memo[ori]=length
    return length
  

memo= {1:0, 2:1}
for num in range (1,1000001):
  Collatz(num,memo)
end= time.time()
print(end-start)
max_key = max(memo, key=memo.get)

      

















    
