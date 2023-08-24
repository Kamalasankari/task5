#removing vowels from a string


def novowl(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = ""

    for i in range(len(s)):
        if s[i] not in vowels:
            result = result + s[i]
    print("After removing Vowels: ", result)
    return result
s = input("enter a string:")
novowl(s)



