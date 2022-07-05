list=[1,2,3,4,5,]
i=0
a=1
b=[]
while i<len(list):
    b.append(a-i)
    i+=1
    a+=1
print(b)