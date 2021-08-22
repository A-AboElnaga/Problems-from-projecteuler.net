import time
def is_num_palindromic(num):
    string = str(num)
    string_rev = string[::-1]
    if string_rev == string:
        return True
    else: 
        return False
start = time.time()

n =3
max_num = ((10**n) -1)
min_num = (10**(n-1))
products = (z * x
            for z in range(max_num, min_num - 1, -2)
            for x in range(max_num, z - 1, -2)
            if z * x % 11 == 0 and is_num_palindromic(z*x))
for product in products:
     end = time.time()
     print(product,f'time:{end-start}')
     
     break
    
        
