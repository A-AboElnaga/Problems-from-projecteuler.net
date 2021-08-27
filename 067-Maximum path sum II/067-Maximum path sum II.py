with open('067-Maximum path sum II.txt') as inputs:
    num = inputs.readlines()

full_list=[]
for elem in num:
    elem= elem.split(' ')
    full_list.append(elem)

def sum_max_path(full_list,summ=0,x=0):
  new_rows=full_list.copy()
  res= 0
  for y in range((len(full_list)-1),-1,-1):
    new_rows[y]=[]
    for x in range(0,len(full_list[y])):
      try: y_c=int(full_list[y-1][x])
      except: y_c = 0
      try:
        x_a=int(full_list[y][x])
        try:
          x_b=int(full_list[y][x+1])
        except: x_b=0
      except: x_a=0
      if y ==0:
        return(full_list[y][0]+res)
      else:
        if x_a+y_c > x_b+y_c :
         try:
          full_list[y-1][x]= (x_a+y_c)
         except: continue
        else:
         try:
          full_list[y-1][x]= (x_b+y_c)
         except: continue
print(sum_max_path(full_list))
