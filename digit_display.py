template = [
        "###", "  #", "###", "###", "# #", "###", "###", "###", "###", "###",
        "# #", "  #", "  #", "  #", "# #", "#  ", "#  ", "  #", "# #", "# #",
        "# #", "  #", "###", "###", "###", "###", "###", "  #", "###", "###",
        "# #", "  #", "#  ", "  #", "  #", "  #", "# #", "  #", "# #", "  #",
        "###", "  #", "###", "###", "  #", "###", "###", "  #", "###", "###"
              ]

#Print hashtags for input numbers, according to template
def lightUp(number):
    display = ""
    for line in range(5):
        display += '\n'
        for digit in number:
            display += (template[((10*line) + int(digit))] + ' ')
    return display + '\n'

#Get input
num = input("Please type a number:")

#Repeat until input contains only number
while not num.isdigit():
    num = input("Sorry, that's not a number! Try again:")

print(lightUp(num))
