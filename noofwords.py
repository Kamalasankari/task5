c = 0
def noofwords(str1):
    c = len(str1.split())
    print("number of words:",c)
    return c


str1 = input("enter the sentence:")
noofwords(str1)
