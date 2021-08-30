def fib(n, memo={}):
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except:
        result = fib(n-1, memo) + fib(n-2, memo)
        memo[n] = result
        return result

if __name__ == '__main__':
  x,y='',2000
  while len(x) <1000:
    y+=1
    x=str(fib(y))
print(y+1)
    
