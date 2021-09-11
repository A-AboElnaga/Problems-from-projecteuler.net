dict1={}
for x in range(2,101):
  for y in range(2,101):
    dict1[x**y]=1
print(len(dict1))
