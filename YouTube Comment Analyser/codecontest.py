# test_list = [["Gfg", "good"], ["is", "for"], ["Best"]]
# print(len(test_list))
# for i in range(len(test_list)):
#     for j in range(len(test_list)):
#         try:
#             print(test_list[j][i],end="")
#         except IndexError:
#             pass

# import itertools as it
# # import operator
# import time

# iterator = list(it.count(start=0,step=2))
# print(iterator)

# lst=[1,2,3,4]
# lst2=lst[:]

# lst[0]=10

# print(lst2)
# print(set(zip(lst,lst2)))

# lst=["yogi","kannah","yogesh"]

# for i,j in enumerate(lst):
#     print(i,j)

# for i in zip(it.count(start=0,step=1),lst):
#     print(i)

# for i in it.count(start=0, step=2):
#     if i<=80:
#         print(i)
#     else:
#         break

# iterator=it.count(start=0,step=20)
# for i in iterator:
#     if i<100000:
#         print(i)
#     else:
#         break


# lst=list(it.repeat(24,10))
# print(lst)

# lst2=[0]*0
# print(lst2)

# import operator
arr=[1,2,3]
arr2=[1,2,3]

# a,b,c=map(operator.mul,arr,arr2)
# print(a,b,c)

# let=["hi","sd","aerqr","rtwe"]
# lsy=list(map(str.upper,let))
# print(lsy)


import itertools as it
import operator

# result=list(it.accumulate(arr,operator.add))
# print(result)

# name=["yogeshkannah"]
# name2=["kalainambi"]

# lst=[]
# # for i in name:
# #     lst.append(i)

# lst=list(it.chain(name,name2))
# print(lst,flush=True)

# num="1234567890"

# nums=list(it.chain(num))

# num2=[[1,2],[3,4]]
# nu=list(map(pow,num2))
# print(nu)

# for i in nu:
#     print(type(i))


# Python code to demonstrate the working of
# compress()


# import itertools
# import operator


# Codes =['C', 'C++', 'Java', 'Python']
# selectors = [False, False, True, True]

# Best_Programming = itertools.compress(Codes, selectors)

# for each in Best_Programming:
# 	print(each)

# lst=[1,2,3,4,5,6,7,8,9]

# iti=iter(lst)

# result=it.tee(iti,10)
# for i in it.tee(iti,10):    
#     print(list(i))

from itertools import zip_longest


x =[1, 2, 3]
y =[8, 9,4]
z = list(zip_longest(x, y,fillvalue='_'))

for (i,j) in zip_longest(x,y):
    print(i,j)
print(z)
