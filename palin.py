#to find given string is palindrome or not
def palindrome(str):
    for i in range(0, int(len(str) / 2)):
        if str[i] == str[len(str) - i - 1]:
            return True
    return False


s = input("enter string:")
ans = palindrome(s)
if ans:
    print("Yes")
else:
    print("No")