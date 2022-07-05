# Write a code that prints the maximum in this list.
a= [50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
while i<len(a):
    b=max(a)
    i+=1
print(b)


num=[50,40,23,70,56,12,5,10, 7]
i=0
a=0
while i<len(num):
    if num[i]>a:
        a=num[i]
    i+=1
print(a)

