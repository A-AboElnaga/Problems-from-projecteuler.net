def sum_spiral_diagonals(length):
  
  start =length*length
  center=str(int(length/2))
  cord= center+','+center
  dict1={cord:1}
  x_max,y_max=length-1,length-1
  x,y=x_max,y_max
  x_min,y_min = 0,0
  
  while start>1:
   if x_max < x_min:
     x_max,x_min=x_min,x_max
   if y_max < y_min:
     y_max,y_min=y_min,y_max
     
   for x in range(x_max,x_min-1,-1):
      cord= str(x)+','+str(y)
      dict1[cord]=start
      start -=1
      
   for y in range(y_max-1,y_min-1,-1):
      cord= str(x)+','+str(y)
      dict1[cord]=start
      start -=1
      
   x_min +=1  
   for x in range(x_min,x_max+1):
      cord= str(x)+','+str(y)
      dict1[cord]=start
      start -=1
   x_max-=1  
   
   y_min+=1
   for y in range(y_min,y_max):
      cord= str(x)+','+str(y)
      dict1[cord]=start
      start -=1
   y_max-=1
      
  
      
  dig1=0
  x,y=length-1,length-1
  while x>-1:
      cord= str(x)+','+str(y)
      dig1+= dict1[cord]
      x-=1
      y-=1
  
  dig2=0
  x,y=0,length-1
  while y>-1:
      cord= str(x)+','+str(y)
      dig2+= dict1[cord]
      x+=1
      y-=1
  return(dig1+dig2-1)

print(f'first method:{sum_spiral_diagonals(1001)}')



#Method 2 Adapted form 'https://www.xarg.org/puzzle/project-euler/problem-28/':
  
def solution(n) :
    return (n * (n * (4 * n + 3) + 8) - 9) / 6;

print(f'second method: {solution(1001)}')
