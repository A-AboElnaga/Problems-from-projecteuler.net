num='''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''
num = (num.split('\n'))
full_list=[]
for elem in num:
    elem= elem.split(' ')
    full_list.append(elem)

# # No need to uncomment this function and its call, at first I thought the problem asked for 
# # the sum of maximum element in each row; and this function do that and I didnot want to delete it
# def sum_max_elems_in_rows(full_list,summ=0,x=0):
#   for y in range(len(full_list)):
#     if y ==0:
#       summ+=int(full_list[y][0])
#     else:
#       if int(full_list[y][x])> int(full_list[y][x+1]):
#         summ+=int(full_list[y][x])
#       else:
#         summ+=int(full_list[y][x+1])
#         x+=1
#   return(summ)
# print(sum_max_elems_in_rows(full_list))  
    


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

  
