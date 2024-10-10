def read_int(prompt, min, max):
    while True:
        inp = input(prompt)
        try:
            x = int(inp)
            assert min <= x <= max
            break
        except ValueError:
            if inp == 'exit':
                return False
            print("Error: wrong input")
        except KeyboardInterrupt:
            return False
        except:
            print("Error: the value is not within the permitted range (" + str(min) + ".." + str(max) + ")")
    return x

while (v := read_int("Enter a number from -10 to 10: ", -10, 10)):
    print("The number is:", v)
