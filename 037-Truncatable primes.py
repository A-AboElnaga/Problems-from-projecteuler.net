def SieveOfEratosthenes(n):
    # Create a list of boolean values where the index represents the value of the number "prime[0..n]"     
    # and initialize all entries as true. A value in prime[i] will
    #finally be false if i is Not a prime, else true.
    
    prime = [True for i in range(n+1)]
    for i in range(4, n + 1, 2):
                prime[i] = False
    p = 3
    while (p * p <= n):
         
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
             
            # Update all multiples of p
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False # '0' is not a prime so set index 0 to False
    prime[1]= False # '1' is not a prime so set index 1 to False
    # Return list of all prime numbers smaller than n
    return prime
  

def is_Truncatable_primes(num,prime_list):
  if prime_list[num]:
    num_str=str(num)
    for x in range(1,(len(num_str)+1)): 
      try:
        if prime_list[int(num_str[0:-x:])]==False:
          return False
        if prime_list[int(num_str[x::])]==False:
          return False
  
      except: continue
    return True
  return False

prime_list = SieveOfEratosthenes(1000001)
res=[]
for x in range (11,1000000,2):
  if is_Truncatable_primes(x,prime_list)==True:
    res.append(x)
print(sum(res))
  
    
