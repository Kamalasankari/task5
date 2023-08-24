# to find frequent character in a string
def freqchar(str1):
    c = {}
    for i in str1:
        if i in c:
            c[i] = c[i] + 1
        else:
            c[i] = 1
    #print(c)
    print(max(c, key=c.get), max(c.values()))
    return c


str1 = input("enter string: ")
freqchar(str1)




