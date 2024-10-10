def encrypt(msg, cipher, act):
    result = ""
    if act == 'B':
        cipher = 26 - cipher
    for char in msg:
        if char.isalpha():
            code = (ord(char) + cipher)
            if char != char.lower():
                if code > ord('Z'):
                    code = ord('A') + (code - ord('Z') - 1)
            elif code > ord('z'):
                code = ord('a') + (code - ord('z') - 1)
            result += chr(code)
        else:
            result += char

    return result

def getMsg():
    message = input("Please enter a message to encrypt:")

    satisfied = 0
    while not satisfied:
        shift = input("Please input a shift value between 1 and 25:")
        try:
            shift = int(shift)
            if 0 < shift < 26:
                satisfied = 1
        except:
            continue
    return [message, shift]

while (input("(De)Cipher another message? ")) != 'no':
    cipher = getMsg()

    satisfied = 0
    action = input("Would you like to:\n(A) encrypt\n(B) decrypt\n")
    if action == 'A' or action == 'B':
        satisfied = 1
    while not satisfied:
        action = input("Please choose either (A) or (B): ")
        if action == 'A' or action == 'B':
            satisfied = 1
    
    print("[" + str(cipher[0]) + "] will be shifted by " + str(cipher[1]) + "\n")
    print(encrypt(cipher[0], cipher[1], action))
