# Q: How to find all pairs in an array of integers whose sum is equal to the given number?
# Output:-
# [[11,19], [12,18],[13,17]]


# number = 30
# n = [10, 11, 12, 13, 14, 17, 18, 19]
# a=[]
# i=0
# while i<len(n):
#     j=0
#     while j<i:
#         if n[i]+n[j]==number:
#             c=n[j],n[i]
#             a.append(c)
#             # a.sort()
#         j+=1
#     i+=1
# print(a)

# n = [10, 11, 10, 13, 11, 17, 13, 19]
# a=[]
# i=0
# while i<len(n):
#     j=0
#     while j<i:
#         if n[j]==n[i]:
#             c=n[j],n[i]
#             a.append(c)
#         j+=1
#     i+=1
# print(a)

list1=[2,3,4,6,7,8,8,7,9]
i=0
a=[]
while i<len(list1)-1:
    c=[]
    c.append(list1[i])
    c.append(list1[i+1])
    a.append(c)
    i=i+2
print(a)




