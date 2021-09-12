import time
start = time.time()
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
  x,y='',1
  while len(x) <1000:
    y+=1
    x=str(fib(y))
print(y+1)
print(f'time:{time.time()-start}')



start = time.time()
def fib1(num,fib_list=[1,1]):
    fib_list.append(fib_list[-1]+fib_list[-2])
    fib_list.pop(0)
    return(fib_list[-1],fib_list)

fib_list=[1,1]
x,y='',1
while len(x) <1000:
  y+=1
  x,fib_list=(fib1(y,fib_list))
  x=str(x)
print(y+1)
print(f'time:{time.time()-start}')
