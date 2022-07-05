# list1=[1,[2,3,4,5],6,7,[8,9]]
# print(list1[1][1])
# print(list1[3])
# print(list1[4][1])


# students_list = ["robin", "anamika", "faisal", "valmiki", "waseem", "amara"]
# i=0
# while i<len(students_list):
#     a=students_list[i]
#     print(i,":",a)
#     i+=1





# list=[1,[2],4,[3,9],[8],5,8,[2,[1]]]
# i=0
# while i<len(list):
#     a=list[i]
#     print(i,"-",a)
#     i+=1

# list1=[1,[2],4,[3,9],[8],5,8,[2,[1]]]
# #

# print(list1[0])
# print(list1[1][0])
# print(list1[2])
# print(list1[3][0])
# print(list1[3][1])
# print(list1[4][0])
# print(list1[5])
# print(list1[6])
# print(list1[7][0])
# print(list1[7][1][0])



test_list = [[5], [9, 3, 1, 4], [3, 2], [4, 7, 8, 3, 1, 2], [3, 4, 5]]
a=[]
l=0
i=0
while i<len(test_list):
    a.append(l)
    l+=len(test_list[i])
    i+=1
print("initial element indice:",(a))


# Iterate over both the values in a list and their indices
# grocery_list = ['flour','cheese','carrots']
# Output: 
#=> 0: flour
#=> 1: cheese
#=> 2: carrots

# g = ['flour','cheese','carrots']
# i=0
# while i<len(g):
#     a=g[i]
#     print(i,":",a)
#     i+=1