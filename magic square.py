# Magic Square is that kind of square in which sum of each row, sum of each column and sum of both the diagonals is equal.

# You have to write this program that takes a nested list as input and checks whether it is a magic square or not?

# This is a magic square because,

# m_square=[
#     [8,3,4],
#     [1,5,9],
#     [6,7,2]
# ]
# i=0
# while i<len(m_square):
#     row=0
#     coulum=0
#     j=0
#     while j<len(m_square):
#         row=row+m_square[j][i]
#         d=0
#         while j<len(m_square):
#             d1=0
#             d2=0
#             c=0
#             while d<len(m_square):
#                 d1=d1+m_square[d][c]
#                 d2=d2+m_square[c][d]
#                 d1=d2
#                 c=c+1
#             d=d+1
#         j=j+1
#     i=i+1
# # print(row)
# # print(coulum)
# # print(row)
# # print(coulum)
# # print(d1)
# # if coulum==row==d1:
# #     print("it is magic square")
# # else:
# #     print("not magic square")

# num=[
#     [8,3,4],
#     [1,5,9],
#     [6,7,2]
# ]
# i=0
# a=0
# b=0
# c=0
# # d=0
# # e=0
# # f=0
# # g=0
# # h=0
# while i<len(num):
#     a=a+num[0][i]
#     b=b+num[1][i]
#     c=c+num[2][i]
#     a+=1
#     b+=1
#     c+=1
#     # d=d+num[i][0]
#     # e=e+num[i][1]
#     # f=f+num[i][2]
#     # g=g+num[i][i]
#     # h=h+num[i][2-i]
#     i+=1
# if a==b==c:
#     print("magic square")
# else:
#     print("not magic square")


# magic_square=[[8,3,4],[1,5,9],[6,7,2]]
# i=0
# while i<len(magic_square):
#     row=0
#     j=0
#     row=0
#     column=0
#     diagonal=0
#     while j<len(magic_square[i]): 
#         row=row+magic_square[i][j]
#         column=column+magic_square[j][i]
#         diagonal=diagonal+magic_square[j][j]
#         j=j+1
#     i=i+1
# print(row,"=sum of row")
# print(column,"=sum of column")
# print(diagonal,"=sum of diagonal")
# if row==column==diagonal:
#     print("magic square")
# else:
#     print("not magic square")


