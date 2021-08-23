def fib(n, memo={}):
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except:
        result = fib(n-1, memo) + fib(n-2, memo)
        memo[n] = result
        return result
res = 0   
for i in range(100000):
    x = fib(i)
    if x > 4000000:
        print (res)
        break
    elif x %2 == 0:
        res += x
        
        
