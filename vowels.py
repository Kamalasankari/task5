# to count number of each vowels in the given string
s = "Guvi Geeks Network Private Limited"
a = 0
e = 0
j = 0
o = 0
u = 0
l = ["a","e","i","o","u","A","E","O","I","U"]
for i in s:
    if i == "a" or i == "A":
        a = a + 1
    if i == "e" or i == "E":
        e = e + 1
    if i == "i" or i == "I":
        j = j + 1
    if i == "o" or i == "O":
        o = o + 1
    if i == "u" or i == "U":
        u = u + 1
print("a=", a,"e=", e,"i=", j,"o=", o,"u=", u)