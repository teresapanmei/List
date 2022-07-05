# Convert Character Matrix to single String;
# 	The original list is: [ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
# The String after join: gfgisbest


cha=[ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
i=0
while i<len(cha):
    j=0
    while j<len(cha[i]):
        print(cha[i][j],end="")
        j+=1
    i+=1
