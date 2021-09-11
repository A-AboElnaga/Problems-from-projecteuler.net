import time
start=time.time()
def fun():
  counter=0
  summ=0
  for a in range(0,10):   
    for b in range(0,10):
      for c in range(0,10):
        for d in range(0,10):
          for e in range(0,10):
            for f in range(0,10):
              counter +=1
              if counter >(6*(9**5)):
                return summ-1
              num=(a**5)+(b**5)+(c**5)+(d**5)+(e**5)+(f**5)
              n= int(str(a)+str(b)+str(c)+str(d)+str(e)+str(f))
              if (num)==n:
                summ+=num
              
print(f'result:{fun()}')
print(time.time()-start)
