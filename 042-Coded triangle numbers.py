import math
import time

start= time.time()

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

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string
    
    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  
    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.
    Returns: a list of all permutations of sequence
    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    word_original = sequence
    word = word_original
    # word = word_original.replace(" ","")              #removes spaces from the word
    # word = word.lower()                               #converts all letters to lowercase     
    word_list = list(word)
    
    if len(sequence) == 1:
        return [sequence]
    else:
        smaller_list = word_list.copy()
        perms=[]
        x= smaller_list[0]
        if len(smaller_list) >1:
            smaller_list.pop(0)   
        smaller_word= "".join(smaller_list)
        fewer_letter_list = get_permutations(smaller_word)
        
        for element in fewer_letter_list:
            listed_letters = list(element)
            counter = 0 
            while counter <= len(listed_letters):
                cpd_lstd_ltr = listed_letters.copy()
                cpd_lstd_ltr.insert(counter,x)
                counter = counter + 1
                new_word= "".join(cpd_lstd_ltr)
                perms.append(new_word)
    final_list= list(dict.fromkeys(perms)) #remove duplicates
    return final_list


list1=[1,2,3,4,5,6,7,8,9]
big=7

for n in range(1,9):
  use=list1.copy()
  use=use[0:n:]
  seq=''.join(str(elm) for elm in use)
  perm_list= get_permutations(seq)
  for perm in perm_list:
    if is_prime(int(perm)):
      if int(perm)> big:
        big = int(perm)
print(big,time.time()-start)
