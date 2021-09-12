#Method1: Brute Force
coins=[1,2,5,10, 20, 50, 100,200]
total=200
ways=0
for a in range(total,-1,-200):
  for b in range(a,-1,-100):
    for c in range(b,-1,-50):
      for d in range(c,-1,-20):
        for e in range(d,-1,-10):
          for f in range(e,-1,-5):
            for g in range(f,-1,-2):
              ways+=1
print(ways) 
  
      
#Method2: Dynamic programing Recursive Depth First Search with Memoization 

def fun(total, coins,const,memo={}):
  if total==0:return 1
  ans=0
  for coin in coins:
    rem= total - coin
    if str(total)+'-'+str(const) in memo:
      return memo[str(total)+'-'+str(const)]
    if rem>=0 and coin>=const:
      ans+= fun(rem,coins,coin)
  memo[str(total)+'-'+str(const)]=ans
  return ans
target=200
print(fun(target,coins,0))
