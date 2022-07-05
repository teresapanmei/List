# Count Occurences
# Occurences - is made from the word occur which means that how many times
# a certain character or word appears.
# Output of the Sample List

# [["a", 6], ["n", 3], ["t", 2], ["x", 2], ["u", 1], ["g", 1]]

# a - 6 times
# n - 3 times
# t - 2 times
# x - 2 times
# u - 1 times
# g - 1 times


list= ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
while i<len(list):
    a=list.count("a")
    b=list.count("n")
    c=list.count("t")
    d=list.count("x")
    e=list.count("u")
    f=list.count("g")
    i+=1
print([["a",a],["n",b],["t",c],["x",d],["u",e],["g",f]])

