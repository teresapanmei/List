# mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
# subStr = "over"
# Output
# the quick brown fox jumped on the lazy dog. the dog slept on the verandah.

# mainstr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
# str=mainstr.split()
# i=0
# while i<len(str):
#     if str[i]=="over":
#         del str[i]
#     else:
#         print(str[i],end="")
#     i+=1
# x= mainstr.replace("over","on")
# print(x)

m = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
i=0
while i<len(m):
    if m[i]=="over":
        del m[i]
    else:
        print(m[i],end="")
    i+=1
a=m.replace("over","on")
print(a)

# m = "the","quick" ,"brown", "fox" ,"jumped", "over", "the" ,"lazy" ,"dog","." ,"the", "dog", "slept", "over", "the" ,"verandah."
# i=0
# while i<len(m):
#     if m[i]=="over":
#         del m[i]
#     else:
#         print(m[i],end="")
#     i+=1
# a=m.replace("over","on")
# print(a)

