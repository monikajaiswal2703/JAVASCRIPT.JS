n=5
a=n
b=n
i=1
while i<=n:
    j=1
    while j<(n*2):
        if j>a and j<b:
            print(" ",end=" ")
        else:
            print("*",end=" ")
        j+=1
    print()
    i+=1
    a-=1
    b+=1