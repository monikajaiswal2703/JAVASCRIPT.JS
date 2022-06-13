size=int(input("enter the size"))
a=[]
for i in range(size):
    num=int(input("enter the number"))
    a.append(num)
for i in range(size):
    for j in range(size-i-1):
        if a[j]>a[j+1]:
            t=a[j]
            a[j]=a[j+1]
            a[j+1]=t
            print("sort arrey is",a)

# size=int(input("enter the size"))
# i=0
# a=[]
# while i<(size):
#     num=int(input("enter the number"))
#     a.append(num)
#     i+=1
# print(a)
# i=0
# while i<len(a):
#     j=0
#     while j<len(a)-1:
#         if a[j]>a[j+1]:
#             t=a[j]
#             a[j]=a[j+1]
#             a[j+1]=t
#         j+=1
#     i+=1
# print("sort array is",a)


# list = [100, 180, 260, 310, 40, 535, 695]
# i=0
# while i<len(list):
#     i=int(input("enter the number"))
#     print(i,list[i])
#     break
# i+=1

# a=[23,45,82,27,66,12,78,13,71,86]
# max=0
# i=0
# while i<len(a):
#     if a[i]>max:
#         max=a[i]
#     i+=1
# print(max,"\n",i-1)

# a=[5,4,3,6,7,8,9,2,3,0,12]
# def sort_list(my_list):
#     even=[]
#     odd=[]
#     for i in my_list:
#         if i%2!=0:
#             odd.append(i)
#         else:
#             even.append(i)
#     odd.sort(),even.sort()
#     return odd+even
# print(sort_list(a))

# a=[5,4,3,6,7,8,9,2,3,0,12]
# e=[]
# odd=[]
# for i in a:
#     if i%2==0:
#         e.append(i)
#     else:
#         odd.append(i)
# print(e+odd)


# a="hello"
# b=input("enterbthe no ")
# count=0
# for i in a:
#         count+=1
# count2=0
# if count==len(b):
#     for i in range(len(b)):
#         if a[i]==b[i]:
#             count2+=1
# if count==count2:
#     print(count*2)

            
# i="hello"
# j="hello"
# if i==j:
#     b=len(i)
#     print(b*2)
# x=2
# def sum():
#     c=2
#     d=7
#     b=c+d
#     return b
# y=2
# print(sum())
# print(66)

# a = [10,8,7,5,9]
# c=0
# max=0
# i=len(a)-1
# b=[]
# while i>=0:
#     if a[i]>max:
#         max=a[i]
#         c=i
#         b.append(c)
#     i-=1
# b.reverse()
# print(b)

# a = [3,8,7,5,2]
# m=0
# i=0
# while i<len(a):
#     if a[i]>m:
#         m=a[i]
#     i+=1
# print(m)
# for i in a:
#     if i>m:
#         m=i
# print(m)

# a = [14,8,7,5,15,11]
# max=0
# i=len(a)-1
# b=[]
# while i>=0:
#     if a[i]>max:
#         max=a[i]
#         b.append(i)
#     i-=1
# b.reverse()
# print(b)

# "cat dog "
# T=int(input())
# for i in range (T):
#     # c,d,l=list(map(int,input().split()))
#     c=int(input("num"))
#     d=int(input("num"))
#     l=int(input("num"))
#     total=(c+d)*4
#     min=max(0,c-d*2)
#     if total>=l and l%4==0 and (d+min)*4<=l:
#         print('yes')
#     else:
#         print("no")

# t=int(input("entert n"))
# for i in range(t):
#     c=int(input("num"))
#     d=int(input("num"))
#     l=int(input("num"))
#     nl=[]
#     if(c<=2*d):
#         nl.append(4*d)
#     else:
#         a=c-2*d
#         nl.append(4*(d+a))
#     nl.append(4*(c+d))
#     if(nl[0]<=l<=nl[1] and l%4==0):
#         print("yes")
#     else:
#         print("no")


# r: 7
# unit: 2
# n: 8
# arr: 2 8 3 5 7 4 1 2"

"using function"
def rat_house(r,unit,arr,n):
    if n==0:
        return -1
    tfr=r*unit
    food=0
    house=0
    for house in range(n):
        food+=arr[house]
        if food >= tfr:
            break
            # print("food is sufficient")
    if tfr > food:
        return ("food is not sufficient")
    return house+1
r = int(input("number of rat"))
unit = int(input("number of unit"))
n = int(input("number of arr"))
arr=[2, 8, 3, 5, 7, 4, 1, 2]
print(rat_house(r,unit,arr,n))

"without function"
# r = int(input())
# unit = int(input())
# n=int(input("enter the list len"))
# b=[]
# for i in range(n):
#     arr=int(input("enter the number"))
#     b.append(arr)
# tfr=r*unit
# food=0
# house=0
# print(b)
# for j in (b):
#     food+=j
#     if food>=tfr:
#         pass
# if tfr>food:
#     print("food is not sufficient")
# else:
#     house+=1
# print(house)

