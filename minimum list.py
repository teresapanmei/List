num=[50,40,23,70,56,12,5,10, 7]
i=0
m=num[0]
while i<len(num):
    if num[i]<m:
        m=num[i]
    i+=1
print(m)
