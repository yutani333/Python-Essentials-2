from os import strerror

try:
    pad = open("testpad.txt", "w+")
except IOError as e:
    print("Couldn't open testpad: ", strerror(e.errno))
    exit(e.errno)

while (line := input("new input line: ")):
    pad.write(line + '\n')

print("Input complete.\ntestpad conent:\n\n")
pad.seek(0)
print('[', pad.read(), ']', sep = '')
