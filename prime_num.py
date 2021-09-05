n = 20

for num in range(1, n + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)


# Output
''' 
2
3
5
7
11
13
17
19 
'''