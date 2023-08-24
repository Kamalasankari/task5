# to find anagram string
def anagrams(inp1, inp2):
    # if the length of the two strings is not the same, they are not anagrams.
    if len(inp1) != len(inp2):
        return False

    # initialize the dictionary
    counts = {}

    # loop simultaneously through the characters of the two strings.
    for c1, c2 in zip(inp1, inp2):
        if c1 in counts.keys():
            counts[c1] += 1
        else:
            counts[c1] = 1
        if c2 in counts.keys():
            counts[c2] -= 1
        else:
            counts[c2] = -1


    for count in counts.values():
        if count != 0:
            return False
    return True
inp1 = input("Enter string1 :")
inp2 = input("Enter string2 :")
print(anagrams(inp1, inp2))
