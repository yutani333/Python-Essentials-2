def isAna(str1, str2):
    if str1 and str2:
        list1 = sorted(list(str1.lower()))
        list2 = sorted(list(str2.lower()))
        if list1 == list2:
            return True

    return False

print("Check is two strings are anagrams.")

another = 1
while another:
    string1 = input("Please input the first string: ")
    string2 = input("Please input the second string: ")

    if isAna(string1, string2):
        print("Yes, they are anagrams.")
    else:
        print("No, they are not anagrams.")
    if (input("Exit program? ")) != 'no':
        another = 0
