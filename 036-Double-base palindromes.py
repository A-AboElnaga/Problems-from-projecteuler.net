def is_num_palindromic(num):
    string = str(num)
    string_rev = string[::-1]
    if string_rev == string:
        return True
    else: 
        return False

list=[]
for x in range(1,1000000):
  if is_num_palindromic(x):
    y=bin(x)
    if is_num_palindromic(y[2::]):
      list.append(x)
      
print(sum(list))
