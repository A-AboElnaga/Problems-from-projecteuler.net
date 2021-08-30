# Method 1: building a function to return all possible permutations


# def get_permutations(sequence):
#     '''
#     Enumerate all permutations of a given string
    
#     sequence (string): an arbitrary string to permute. Assume that it is a
#     non-empty string.  
#     You MUST use recursion for this part. Non-recursive solutions will not be
#     accepted.
#     Returns: a list of all permutations of sequence
#     Example:
#     >>> get_permutations('abc')
#     ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
#     Note: depending on your implementation, you may return the permutations in
#     a different order than what is listed here.
#     '''
#     word_original = sequence
#     word = word_original
#     # word = word_original.replace(" ","")              #removes spaces from the word
#     # word = word.lower()                               #converts all letters to lowercase     
#     word_list = list(word)
    
#     if len(sequence) == 1:
#         return [sequence]
#     else:
#         smaller_list = word_list.copy()
#         perms=[]
#         x= smaller_list[0]
#         if len(smaller_list) >1:
#             smaller_list.pop(0)   
#         smaller_word= "".join(smaller_list)
#         fewer_letter_list = get_permutations(smaller_word)
        
#         for element in fewer_letter_list:
#             listed_letters = list(element)
#             counter = 0 
#             while counter <= len(listed_letters):
#                 cpd_lstd_ltr = listed_letters.copy()
#                 cpd_lstd_ltr.insert(counter,x)
#                 counter = counter + 1
#                 new_word= "".join(cpd_lstd_ltr)
#                 perms.append(new_word)
#     final_list= list(dict.fromkeys(perms)) #remove duplicates
#     return final_list
# final_list =sorted(get_permutations('0123456789'))
# print(final_list[999999])






#Method 2: using built-in functions

import itertools

# We initialize a list as the lowest permutation of the given digits, which is the sequence
# (0,1,2,3,4,5,6,7,8,9). Then we call a Python library function that generates a stream of
# all permutations of the values, seek to the 999 999th element (0-based indexing), and stringify it.
arr = list(range(10))
temp = itertools.islice(itertools.permutations(arr), 999999, None)
print( "".join(str(x) for x in next(temp)))
