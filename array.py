# Q: Given two arrays, 1,2,3,4,5 and 2,3,1,0,5 find which numbers are 
# not present in the second array.



l1 = [1,2,3,4,5]
l2 = [2,3,1,0,5]
i=0
a=[]
while i<len(l1):
    if l1[i] not in l2:
        a.append(l1[i])
    i+=1
print(a)
