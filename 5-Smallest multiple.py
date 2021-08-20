import time
start = time.time()
result =1
Factors_list =[]
LCM_list=[] #Least Common Multiple (LCM)

for num in range(1,21):
    value = num
    x =2
    while num > 1:
        while num%x == 0:
            num = num / x
            Factors_list.append(x)
        if num%x != 0:
            x = x+1
    for element in Factors_list:
        while Factors_list.count(element) > LCM_list.count(element) :
            LCM_list.append(element)
    Factors_list =[]
for factor in LCM_list:
     result = result * factor
end = time.time()
print (result)
print(end - start)
