# "by user input sum of max and min"
# n=int(input("enter the number"))
# nums = list(map(int,input("creat a list").split()))	
# # nums.sort()
# print(nums)
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]>nums[j]:
#             nums[i],nums[j]=nums[j],nums[i]
# print("sort arrey is",nums)
# b=[]
# for k in nums:
#     if k not in b:
#         b.append(k)
# print(b)
# sum=b[n-1] + b[-n]
# print(sum)

# def max_min(data):
#     l = 0
#     s = data[0]
#     for num in data:
#         if num> l:
#             l = num
#         elif num< s:
#             s = num
#     return l+s
# print(max_min([10, 15, 40, -5, 42, 17, 28, 75]))


# "runner up question"
# nums =(map(int,input("enter number").split()))	
# print(nums)
# print (sorted(set(nums))[-2])

# lis = list(map(int,input("enter").split()))
# z = max(lis)
# while max(lis) == z:
#     lis.remove(max(lis))
# print (max(lis))

# "runner up without function"
nums = list(map(int,input("enter number").split()))	
print(nums)
# b=[]
# for i in nums:
#     if i not in b:
#         b.append(i)
# print(b)
# max=0
# for j in b:
#     if j>max:
#         max=j
# print(max)
# max1=0
# for k in b:
#     if k>max1:
#         if max!=k:
#             max1=k
# print(max1)

# "find LCM AND HCF"
# a = int(input("enter the first number: "))
# b = int(input("enter the second number: "))
# HCF = 1
# for i in range(2,a):
#     if(a%i==0 and b%i==0):
#         HCF = i
# print("first number is: ",a)
# print("second number is: ",b)
# print("HCF of the numbers is: ",HCF)



# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# HCF = 1
# for i in range(2,a+1):
#     if(a%i==0 and b%i==0):
#         HCF = i
# print("First Number is: ",a)
# print("Second Number is: ",b)
# LCM = int((a*b)/(HCF))
# print("LCM of the two numbers is: ",LCM)

# n = int(input("Enter a number: "))
# # print("Even", (n % 2 == 0), "Odd",(n % 2 != 0))
# print("Even"*(n % 2 == 0), "Odd"*(n % 2 != 0))

# a=[1,2,[4,5,[3,4],[1,2],4,7]]
# i=0
# b=[]
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             b.append(a[i][j])
#             j+=1
#     else:
#         b.append(a[i])
#     i+=1
# print(b)

# a=[[1,2,3,4],[5,6],[3,4,5]]
# i=0
# c=1
# max=a[i]
# while i<len(a):
#     if len(max)>len(a[i]):
#         max=a[i]
#         # length=len(a[i])
#         c=c+1
#     i+=1
# print(max,c)










# print(a[0]+a[1][0][1])
# b=[]
# for i in a:
#     if type==i:
#         b.append(i)
# # for j in b:
# #     if type==j:
#         print(i)
# #     if type==i:
#         b.append(i)
# print(b)



# a=[[1,2],[3,4],[4,6],[7,8],[9,5]]
# print(a[0]+a[1]+a[2]+a[3]+a[4])
# i=0
# b=[]
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         b.append(a[i][j])
#         j+=1
#     i+=1
# print(b)