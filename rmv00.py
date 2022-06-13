"remove 000 in list"
# a=[10,202000,13000,4047000,100,10230000]
# i=0
# c=[]
# while i<len(a):
#     while a[i]>0:
#         if a[i]%10!=0:
#             c.append(a[i])
#             break
#         a[i]//=10
#     i+=1
# print(c)

import operator
from os import remove


# d={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# dic=sorted(d.items(),key=lambda a:a[1])
# print("assending order",dict(dic))

# s1=dict(sorted(d.items(),key=operator.itemgetter(1),reverse=True))
# print("dessendig order",s1)
# for i in d:
#     for j in d:
#         if d[i]<d[j]:
#             d[i],d[j]= d[j],d[i]
# print(d) 

# a={"a":1,"b":2,"c":3,"d":4}
# k=input("enter the key")
# if k in a:
#     print(a.pop(k))
# else:
#     v=int(input("enter value"))
#     a.update({k:v})
# print(a)

