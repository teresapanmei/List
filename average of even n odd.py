# Write a code that works for any list, it shows the two averages as the output. 
# One is the average of even numbers and the other is the average of odd numbers
# from the given list.


elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum=0
avg=0
even=0
odd=0
while i<len(elements):
    a=elements[i]
    if elements[i]%2==0:
        sum=sum+a
        avg=sum/a
        even+=1
    else:
        sum=sum+a
        avg1=sum/a
        odd+=1
    i+=1
print("even=",even)
print("avg of even=",avg)
print("odd=",odd)
print("avg of odd=",avg1)
