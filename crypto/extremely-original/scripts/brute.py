key=[35, 58, 29, 60, 7, 46]
m=64
a=0
c=0
for possible_a in range(m):
    for possible_c in range(m):
        valid=True
        for i in range(len(key)-1):
            if (key[i+1]!=(possible_a*key[i]+possible_c)%m):
                valid=False
        if valid:
            a=possible_a
            c=possible_c
print("LCG Parameters: a = "+str(a)+", c = "+str(c)+", m = "+str(m))
