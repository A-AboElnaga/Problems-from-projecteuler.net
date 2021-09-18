#Expected results:{1:1,2:1,3:5,4:15,5:105,6:210,7:210,8:1470,9:11760,10:11760,11:11760,12:0} 
#all bigger than 12 is = 0



import time
if __name__ == '__main__':

#Method 1, Brute force : First stores the sequance and then gets the value based on index of the stored sequance
#This is definitely the the worst in terms of time and space order
#0.109 seconds for maxm=6, 4-5 seconds for maxm=7, and much more time for maxm >7

  start = time.time()
  num= '0'
  maxm=7
  if maxm <= 7:  #Limiting the test to maxm = 7 and less
  #beacuse it wil take much more time for bigger values
    for x in range(1,999999999): 
      if len(num)<(10**(maxm)):
          num+=str(x)
      else: break
    
    product=1
    for f in range (maxm):
      product*= int(num[(10**f)])
    
    print(product,time.time()-start)

#Method 2, Brute force : Does not store the sequance but rather gets the value while increasing the length
#This is better than method 1 in terms of space order, but still bad in terms of time order
# 0.199 seconds for maxm=7, 1-2 seconds for maxm=8 , 20-25 seconds for maxm=9
  
  start = time.time()
  length=0
  f=0
  product=1
  if maxm <=9:#Limiting the test to maxm = 9 and less
  #beacuse it wil take much more time for bigger values
    for x in range(1,999999999):
      if length<(10**(maxm-1))+1:
        x_str= str(x)
        if length <10**f and length+len(x_str) >=10**f:
          product*= int(x_str[10**f-length-1])
          f+=1
        length +=len(x_str)
      else: break
      
    print(product,time.time()-start)


#Method 3, Targeted soultion: jumps to (9;99;999;9999..etc) or to the number that gives the exact length or immediatly before it
#This is definitely a lot better in terms of time and space order
# 0.0 seconds for maxm=14 and less, and up to maxm=2570 in less than one second

start = time.time()

max_count=maxm-1
current_number =1
p=1
current_length=1
list=[]
f=0
while f <= max_count:
    if f==0:
        list.append(1)
    else:
      max_num =(10**p)-1
      length_increment=((10**f)-current_length)
      if len(str(current_number))*(max_num-current_number)<= length_increment:
        current_length+=len(str(current_number))*(max_num-current_number)
        current_number=max_num
        if current_length==10**f:
          new_num=str(current_number)[-1]
          list.append(new_num)
        if current_length<10**f and current_length + len(str(current_number+1))>=10**f:
          char_postion= 10**f - current_length -1
          current_number+=1
          current_length+=len(str(current_number))
          list.append(str(current_number)[char_postion])
      else: #len(str(current_number))*(max_num-current_number)> length_increment:
        num_steps=length_increment//len(str(current_number))
        current_length+= num_steps*len(str(current_number))
        current_number += num_steps
        if current_length==10**f:
          new_num=str(current_number)[-1]
          list.append(new_num)
        if current_length<10**f and current_length + len(str(current_number+1))>=10**f:
          char_postion= 10**f - current_length -1
          current_number+=1
          current_length+=len(str(current_number))
          list.append(str(current_number)[char_postion])
      if current_number >= max_num:
        current_number+=1
        current_length+=len(str(current_number))
        p+=1
          
    f= len(list)
res=1
for el in list:
 res*= int(el)    
print (res,time.time()-start)
   
