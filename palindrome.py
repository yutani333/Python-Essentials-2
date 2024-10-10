def isPal(strng):
    reverse = ""
    for char in strng:
        reverse = char + reverse
    if (strng):
        if strng == reverse:
            return True
    return False

print("Check if a string is a palindrome\n")

another = 1
while another:
    candidate = input("Input string: ")
    if isPal(candidate):
        print("Yes, it is a palindrome.")
    else:
        print("No, it is not a palindrome.")
    if (candidate := input("Another test? ")) == 'no':
        another = 0
