dict={}
for x in range (10,99):
  for y in range(x+1,100):
    str_x= str(x)
    str_y=str(y)
    for char in str_x:
      if char in str_y :
        if char !='0':
          x_int=int(str_x.replace(char,'',1))
          y_int=int(str_y.replace(char,'',1))
          try:
            if (y/x)== (y_int/x_int):
              dict[x]=[x_int, y_int]
          except: continue
doms=1
nums=1
for key in dict:
  doms*=dict[key][-1]
for key in dict:
  if doms %dict[key][0]==0:
    nums*=dict[key][0]   
print(doms/nums)
