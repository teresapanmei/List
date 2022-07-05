marks = ["10", "32", "42", "65", "67", "89", "76", "38", "67"]
i=0
counter = 0
total_marks =0
while i < len(marks):
    counter = counter + i
    total_marks = total_marks + counter[i]  
    i+=1
print(total_marks)