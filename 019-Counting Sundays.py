def is_it_Sunday(day):
  day= day% 7
  if day==0:
   return(True)
  else:
    return(False)

months= {1:31,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
Febs={1900:28,1901:28,1902:28,1903:28,1904:29}
days={0:'Sun',1:'Mon',2:'Tues',3:'Wed',4:'Thu',5:'Fri',6:'Sat'}

for i in range (1904,2001):
  if (i-1904)%4 ==0:
    if (i -1904) != 100:
      Febs[i]=29
  else:
      Febs[i]=28
    

start_day = 2 # '2' here indicates that it is Tuesday from the dict of days I created not that it is first day of the month
start_month=1
start_year=1901
year = start_year
day=start_day
Sundays_counter=0
while year <2001:
  for month in range(1,13):
    if month!=2:
      day+= months[month]
    else:
      day+=Febs[year]
    if is_it_Sunday(day): 
      Sundays_counter+=1
  year +=1
  day = day % 7
print(Sundays_counter)
  



  
