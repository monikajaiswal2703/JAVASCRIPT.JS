# i=2
# j=3
# k=i/j*j
# l=j/i*j
# a=i/j*j
# b=j/i*i
# print("%d%d%f%f\n",k,l,a,b)


# a=[1,"monika",1.8]
# b=(1,"mona",2,55)
# # print(a[0:3:2])
# print(list(a+b))
# a.extend(b)
# print(a)

# def diff(a):
#     for i in range(a):
#         if i-i+1==1:
#             return(True)
#         else:
#             return(False)
# print(diff([1,2,3,4,5,6]))


# a=[1200,200,3400,1030,94000]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     while j<a[i]:
#         if a[j]%10==0:
#         # print(a[i][j])
#             b.append(a[j])
#         j+=1
#     i+=1
# print(b)

# a=[1,1,2,2,3,3,4,4,5,5,6,6,6,9,]
# s=set(a)
# a=list(s)
# print(a)

# 10,user input again 1 user input and cheak in first list"
# i=0
# a=[]
# while i<10:
#     num=int(input("enter the number"))
#     i+=1
#     a.append(num)
# print(a)
# num1=int(input("enter the number"))
# if num1 in a:
#     print(num1, "is present a" )
# else:
#     print(num1,"not present ")

# 15,"removing even number"
# list = [1,2,3,4,5,6,7,8,9,10,12,21,13,31,14,41,15,51,61,16,72]
# i=0
# while i<len(list):
#     if i%2!=0:
#      print(i,end=" ")
#     else:
#         pass
#     i+=1
     

# a="My name is Monika"
# b=a.split()
# # print(b)
# i=0
# while i<len(b):
#     c=b[-i-1]
#     i+=1
#     print(c,end=" ") 

# Given the start and end of a range, write a Python program to print all negative numbers in a given range.
# Example:
# Input: start = -4, end = 5
# Output: -4, -3, -2, -1

# for i in range(-4,9,1):
#     print(i,end=" ")
#     if i==-1:
#         # pass
#         break

# a=["zero","one","two","three","four","five","six","seven","eaight","nine",]
# num=input("enter the number")
# i=0
# while i<len(num):
#     k=int(num[i])
#     print(a[k])
#     i+=1

# a="monika jaiswal"
# b="shivani mehta"
# c=a+b
# print([c])
# print(a,b)
# print("",a+"",b)
   
# a=[1,2,"true",3.0,5+2j,34]
# a[2]="apple"
# print(a)


"diffrence between elsement"
# j=[2,45,56,78,98,65,9]
# i=1
# a=[]
# k=0
# while i<len(j):
#     c=j[i]-j[k]
#     a.append(c)
#     i+=1
#     k+=1
# print(a)



# def diff(j):
#     i=1
#     a=[]
#     k=0
#     count=0
#     while i<len(j):
#         c=j[i]-j[k]
#         if c==1:
#             count+=1
#         else:
#             pass
#         i+=1
#         k+=1
#     if count==1:
#         return True
#     return(False)
# print(diff([2,3,56,78,98,65,9]))


# a=[1,2,2,3,5,5]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     c=1
#     while j<len(a):
#         if a[i]==a[j] and i!=j :
#            c+=1
#         j+=1
#     if c>=2:
#         pass
#     else:
#         b.append(a[i])
#     i=i+1
# print(b)

# a=[[1,2,3,4],[5,6],[3,4,5]]
# i=0
# # c=1
# max=a[i]
# while i<len(a):
#     if len(max)<len(a[i]):
#         max=a[i]
#         # length=len(a[i])
#         # c=c+1
#     i+=1
# print(max)

# a={"name":"monika","age":21,"surname":"jaiswal"}
# print(a.popitem())
# print(a)

# a={"name":"monika","age":21,"surname":"jaiswal"}
# b=a.pop("age")
# print(a)

# d = {'k1': 1, 'k2': 2, 'k3': 3}

# d.clear()
# print(d)
# {}


# d = {'k1': 1, 'k2': 2, 'k3': 3}

# removed_value = d.pop('k1')
# print(d)
# # {'k2': 2, 'k3': 3}

# print(removed_value)
# 1

# d = {'k1': 1, 'k2': 2, 'k3': 3}
# del d['k2']
# print(d)
# {'k1': 1, 'k3': 3}


# d = {'k1': 1, 'k2': 2, 'k3': 3}

# del d['k1'], d['k3']
# print(d)

# d = {'k1': 1, 'k2': 2, 'k3': 3}
# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ("red", "white", "blue")
# }

# print(thisdict)

# x = ('key1', 'key2', 'key3')
# y = 4
# thisdict = dict.fromkeys(x, y)
# print(thisdict)

# x = ('key1', 'key2', 'key3')
# y = 1,24,4
# a={}
# thisdict = a.fromkeys(x, y)
# # print(thisdict)

# thisdict['name']="monika"
# print(thisdict)

# x = ('key1', 'key2', 'key3')
# thisdict = dict.fromkeys(x,9)
# print(thisdict)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.setdefault("color", "white")
# car.setdefault("yeaR", "white")
print(car)