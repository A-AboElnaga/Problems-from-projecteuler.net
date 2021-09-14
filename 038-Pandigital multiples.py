pandigital='123456789'
dict={}
def is_pandigital(product_list,pandigital='123456789'):
  product_list= sorted(product_list)
  concatenated=''
  for el in product_list:
    concatenated+=str(el)
  concatenated=''.join(sorted(concatenated))
  if len(concatenated)>9:
      return False
  if concatenated == pandigital:
       return True
      


def search():

  for x in range(99999+1,0,-1):
      product_list=[]
      length=0
      x_str=str(x)
      maxm= str(int(9/(2*len(x_str)))+1)
      f_max=int(int(maxm)*'9')
      
      for factor in range(1,f_max+1):
        factor_str=str(factor)
        
        if len(x_str)*2+ len(factor_str) >9:
          break
        
        else:
          if length < 9:
            product_list.append(x*factor)
            length+=len(str(x*factor))
          else:
            break
        
      if is_pandigital(product_list)==True:
        return (product_list)
result=''   
for el in search():
    result+=str(el)
print(result)
      
        
        
      
    
