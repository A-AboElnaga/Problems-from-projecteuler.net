#BruteForce
summ , sq_sum = 0, 0
for x in range(101):
    summ += x
    sq_sum = sq_sum+(x*x)
print((summ*summ)-sq_sum)


#The_right_way
n=100
summ =n*(n+1)/2
sq_sum=(n*(n+1)*(2*n+1))/ 6
print((summ*summ)-sq_sum)
