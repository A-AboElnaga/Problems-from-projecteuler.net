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
perms= get_permutations('0123456789')
res=[]
for num in perms:
  num_str=str(num)
  if int(num_str[1:4])%2==0:
      if int(num_str[2:5])%3==0:
        if int(num_str[3:6])%5==0:
          if int(num_str[4:7])%7==0:
            if int(num_str[5:8])%11==0:
              if int(num_str[6:9])%13==0:
                if int(num_str[7:10])%17==0:
                  res.append(num)
summ=0
for num in res:
    summ+=int(num)
print(summ)             
      
