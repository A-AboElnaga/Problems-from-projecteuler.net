big=0

for p in range(2,1001,2):
  counter=0
  for a in range(1,int(p/2)):
    b= int((p*(p-(2*a)))/(2*(p-a)))
    if b >=p/2:
      break
    c= p-(a+b)
    if c>a and c>b and c<a+b:
        a_sqr =a**2
        b_sqr =b**2
        c_sqr =c**2
        if ((a_sqr+b_sqr)==c_sqr):
          counter+=1
  if big < counter:
    big =counter
    par=p
print(par)





    
        
