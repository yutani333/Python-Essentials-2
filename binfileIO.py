from os import strerror

data = bytearray(10)

#while (act := input("Action: ")) != 'exit':

for i in range(len(data)):
    data[i] = 10 + i

    try:
        bf = open('bin_file.bin', 'ab')
        bf.write(data)
        bf.close()
    except IOError as e:
        print("I/O error occurred:", strerror(e.errno))

try:
    file = open('bin_file.bin', 'rb')
    cont = bytearray(10)
    file.readinto(cont)
    file.close()

    for b in cont:
        print(hex(b), end=', ')
    print()
    print("File content: " + str(cont))
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
