import math


def get_permutations(sequence):
    '''
    return all rotations of the sequance
    get_permutations(sequence)
    >>> get_permutations('abc')
    ['abc', 'bca', 'cab']
    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    final_list=[]
    for x in range(len(sequence)):
      final_list.append(sequence)
      sequence= sequence[1::]+sequence[0]
    return final_list
  
  
def is_prime(num, primelist=[2, 3]):
       '''enter (num) an intger larger than or equal to 2 and returns True if prime, and False if not'''
       d= 3
       if num == 2:
         return (True)
       if num % 2 == 0:
         return(False)
       while d <= ((int(math.sqrt(num)))+1):
         if num % d == 0 :
          return(False)
         else:
           d += 2
       return True



def no_evens_or_fives(num,evens=[0,2,4,6,8,5]):
  for even in evens:
    if str(even) in str(num):
      return False
  return True


def unique_primes():
  dict={}
  for x in range(3,199999,2):
    if no_evens_or_fives(x)==True:
      if is_prime(x)==True:
        x_str=str(x)
        dict[(x_str)]=1
  return dict
      
dict=unique_primes()

def res(dict):
  reslt=dict.copy()
  reslt[2]=1
  reslt[5]=1
  for key in dict:
    perm_list=get_permutations(str(key))
    for elm in perm_list:
      if is_prime(int(elm))==False:
        reslt.pop(key)
        break
  return reslt

reslt= res(dict)
final={}
for key in reslt:
  x=get_permutations(str(key))
  for element in x:
    final[element]=1

print(len(final))




    
  
  
      
    
