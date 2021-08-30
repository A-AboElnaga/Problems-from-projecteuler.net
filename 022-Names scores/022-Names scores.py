import string

with open('022-Names scores.txt','r') as data:
  names=''+ data.read()
  names =sorted(names.split(','))
  

name_position = 0
tot=0

for name in names:
     name=name.lower()
     name=name.replace('"','')
     name_value=0
     name_position+=1
     for char in name:
       name_value += string.ascii_lowercase.index(char) +1
     tot += (name_position*name_value) 
print(tot)
