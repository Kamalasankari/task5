# to print the unique character the string
n = 0
def unichar(s):
    n = 0
    n = len(set(s))
    print(n)
    return n


s = input("enter string:")

unichar(s)
