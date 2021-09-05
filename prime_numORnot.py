while True:
    n = int(input('Enter the Number:'))
    prime='r'  
    for i in range (2,n):
        if n% i == 0:
            prime = 'fail'
            break    
    if prime=='fail':
        print(n,'is not prime')
    else:
        print(n,'is prime')
        
# Output
'''
Enter the Number:17
17 is prime
Enter the Number:9
9 is not prime
'''