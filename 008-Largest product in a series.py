num =("""
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450""".replace("\n", ""))
num= ''.join(num).split('0')    #Splits the 1000-digits at the zeros
newlist =[]
dic= {}                         #dictionary that will contain the possible combination and its product 
big =1
num_adjacent_digits =13           #Change to change the length of adjacent digit
try: 
  for element in num :            #Case0 sample product = 0  #Ignoring all combinations that would have included at least one zero 
   if len(element) >=num_adjacent_digits: 
     newlist.append(element)
  for element in newlist:         #working with each possible sample
    product =1
    if len(element) ==num_adjacent_digits:         #Case1: sample length = num_adjacent_digits =13
  
     for n in element:
      n=int(n)
      product *= n
    else:                         #Case2: sample length >num_adjacent_digits =13
      scan_min,scan_max=0,(num_adjacent_digits-1)     #Scanners to call the 'num_adjacent_digits=13' adjacent digits (note: could use only one variable but preferred not to)
      while (scan_max+1) <= len(element):
        product =1
        comb=''
        for char in element[scan_min:scan_max+1]:
          comb += char
          char=int(char)
          product *= char
        scan_min +=1
        scan_max +=1
        dic[comb] = product
        if product > big:
          big = product
          stored = comb
    if product >1 and len(element)==num_adjacent_digits:
     dic[element] = product
    if product > big:
      big = product
      stored = element
  print(dic)
  print(f' The {num_adjacent_digits} adjacent digits that have the greatest product:{stored} and their product is :{big}')
except:
  print('Either you have entered num_adjacent_digits larger than possible, or all possiblities have product = 0')
