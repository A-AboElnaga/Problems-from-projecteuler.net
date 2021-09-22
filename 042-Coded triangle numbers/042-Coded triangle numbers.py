letters_dict={'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

Tri_numbers=[]
for n in range(1,50): #Assuming all letters are z and the word is 20 letters, the sum is 520;
#t50=1225 which is way larger than the limit
  tn = 0.5*n*(n+1)
  Tri_numbers.append(int(tn))
  
Res=[]
with open('p042_words.txt','r') as data:
  words=''+data.read()
  words= words.split(',')
  
for word in words:
  word= word.lower()
  word=word.replace('"', '')
  value=0
  for letter in word:
      value+= letters_dict[letter]
  if value in Tri_numbers:
    Res.append(word)

    
      
      
