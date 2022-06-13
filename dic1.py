# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# dic={}
# for i in (dic1,dic2,dic3):
#     dic.update(i)
# for i in dic:
#     if i in dic1:
#         if i in dic2:
#             dic.update({i:dic1[i]+dic2[i]})
# print(dic)


# dict1 =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# # a=dict1.values()
# # print((a))
# c=0
# for i in dict1:
#     for j in range(len(dict1[i])):
#         c+=1
# print(c)

# "without user find min key list"
# dictt = {'V': [10, 12],'VI': [10],'VII': [10, 20, 30, 40],'VIII': [20],
# 'IX': [10,30,50,70],'X': [80]}
# m=1
# d=[]
# for i ,j in dictt.items():
#     if len(j)==m:
#         d.append(i)
# print(d)

# dic= {1: 'NAVGURUKUL',2: 'IN',  3:{'A' : 'WELCOME','B' : 'To','C' : 'DHARAMSALA'}}
# del dic[3]["A"]
# print(dic)
# print(len(dic))


# n=int(input('enter the num ot rows:'))
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print((i), end=" ")
#         j+=1
#     print()
#     i+=1
# k=1
# i=1
# while i<=5:
#     a=1
#     while a<=5-i:
#         print(" ",end = " ")
#         a=a+1
#     j=1
#     while j<=k:
#         print((k),end = " ")
#         j=j+1
#     k=k+1
#     print()
#     i=i+1



# n=int(input("enter the number"))
# count=0
# i=1
# while (i<=n):
#     if (n%i==0):
#         count=count+1
#     i=i+1
# if (count==2):
#     print("prime number")
# else:
#     print("not prime number")

# list=[1,2,3,4]
# n=dict={}
# for i in list:
#     dict[i] = {}
#     dict=dict[i]
# print(n)


# a={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# for i in (a):
#     a[i].clear()
# print(a)

# output={10: 'Theodore', 11: 'Mathew', 9: 'Roxanne'}
# students = {'Theodore': 10,'Mathew': 11,'Roxanne': 9,}
# d={}
# for i in students:
#     d.update({students[i]:i})
# print(d)

# from itertools import combinations
# com_dic = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# lis=[]
# for i in range(1,len(com_dic)):
#     for x in combinations(com_dic,i):
#         dic={z:com_dic[z] for z in x}
#         lis.append(dic)
# print (lis)            



# my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# print(my_dict.keys())
# for i in range(len(my_dict[list(my_dict.keys())[0]])):
#     print(*[str(x[i]) for x in my_dict.values()])


# my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# l=[]
# for i,j in my_dict.items():
#     print(i,end=" ")
#     l.append(j)
# print()
# for i in range(0,len(l)):
#     for j in range(0,len(l)):
#         print(l[j][i],end=" ")
#     print()

d="w3resorces"
b={}
for i in d:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print(b)