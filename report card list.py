marks=[[76,45,87,23,11],[34,12,78,88,45],[86,54,87,90,45]]
i=0
sum=0
while i<len(marks):
    j=0
    while j<len(marks[i]):
        sum=sum+marks[i][j]
        j=j+1
    i=i+1
print("total marks:",sum)


