import time
# Method 1: Brute force with limit of 9999 as a 4 digit multiplied by an integer, 1 for example, will result in a 4 digit product; therefore a total of 9 digits and we need no more
dict1={}
summ=0
start= time.time()
for x in range(1,9999):
 for y in range(1,9999):
    num1= str(x)
    num2= str(y)
    res="".join(sorted(num1+num2+str(x*y)))
    if len(res)>9: break
    if res=='123456789':
      dict1[x*y]=1
for key in dict1:
  summ+=(key)
print(summ)
print(time.time()-start)
  
  
#Methos 2:Building a function to return all possible permutations (not efficient)

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
start= time.time()
  
dict1={}
summ=0
final_list =sorted(get_permutations('123456789'))
for x in range(1,9):
 for y in range(1,9):
  if x>9-(x+y) or y >9-(x+y):
     break
  for element in final_list:
    num1= int(element[0:x])
    num2= int(element[x:x+y])
    product=int(element[x+y::])
    if num1*num2==product:
      dict1[num1*num2]=1
for key in dict1:
  summ+=key
print(summ)
print(time.time()-start)

  
  
  
