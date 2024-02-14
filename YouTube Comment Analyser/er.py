        # """ inverted pattern """

# n=int(input("enter the number"))
# ctr=0
# for a in range(n):
#     for b in range(a):
#         print("*",end=" ")
#     print() 

# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     print()

            # g pattern 

# n=int(input("enter the number of rows:  "))
# for i in range(n):
#     for j in range(n):
#         if (i==0 and (j>=1 and j<n//2+1) ):
#             print("*",end=" ")
#         elif ((i>=1 and i<n-1) and j==0):
#             print("*",end=" ")
#         elif (i==n//2 and (j>1 and j<n//2+1)):
#             print("*",end=" ")
#         elif(i==n-1 and (j>=1 and j<n//2+1)):
#             print("*",end=" ")
#         elif((i>=n//2 and (j==n//2+1)) and i!=n-1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# lst=[1,2,3,0,1,0,1,6,34,0,1,5,4]

# max1=lst[0]
# # lst1=[]
# result=0
# for i,j in enumerate(lst):
#     if max1<j:
#         max1=j
#         # lst1.append(i)
#         result=i
# print(max1)
# print(result)


# for i in zip([1,2,3],[4,5,6]):
#     print(i)

from googletrans import Translator, constants
from pprint import pprint

translator = Translator()

translation = translator.translate("என் பெயர் யோகேஷ்கண்ணா")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

