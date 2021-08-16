#1, 2, 1, 3, 2, 5, 3, 7, 5, 11, 8, 13, 13, 17, …
#1   1   2   3  5 8  13 odd=fib 5=3 7=4
#2 3 5 7 11 13 17  even=prime 8=4
n=int(input())
if n%2!=0:
    g=n//2+1
    a,b=1,1
    if g==1 or g==2:
        print(1)
    else:
        for i in range(g-2):
            c=a+b
            a=b
            b=c
        print(c)
else:
    g=n//2
    i=1
    c=0
    while c<g:
        i+=1
        m=0
        for j in range(1,i+1):
            if i%j==0:
                m+=1
        if m==2:
            b=i
            c+=1
        else:
            pass
    print(b)     
    
"""
o/p
10
11
7
3"""

    
