n = int(input())
m = int(input())

if(n < m):
    while(n <= m):
        print(n, round((n-32)*5/9,1))
        n += 1
        
else:
    while(n >= m):
        print(n, round((n-32)*5/9,1))
        n -= 1
        
    

