# Write a Code that finds second maximum element from the list and print it 
a=[50, 40, 23, 70, 99, 12, 5, 10, 7]
i=0
while i<len(a):
    a.sort()
    i+=1
print("The second max number is:",a[-2])


# num=[50,40,23,70,99,12,5,10, 7]
# l=num[0]
# s=num[0]
# i=0
# while i<len(num):
#     if num[i]>l:
#         l=num[i]
#     i+=1
# i=0
# while i<len(num):
#     if num[i]>s and num[i]!=l:
#         s=num[i]
#     i+=1
# print(s)




