
a = [-10, -3, 5, 6, -2]  # [-10,-3]

max1 = 0
result = [] 
for i in range(len(a)-1):
   b = a[i] * a[i+1] 
   if(b>max1):
       max1 = b
       result = [a[i], a[i+1]]
print(result)