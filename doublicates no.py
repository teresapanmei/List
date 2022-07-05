# n=[1, 2, 2, 5, 8, 4, 4, 8]
# a=[]
# i=0
# while i<len(n):
#     if n[i] not in a:
#         a.append(n[i])
#     i+=1
# print(a)

def check():
    n=[1, 2, 2, 5, 8, 4, 4, 8]
    a=[]
    i=0
    while i<len(n):
        if n[i] not in a:
            a.append(n[i])
        i+=1
    print(a)
check()
