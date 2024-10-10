from sys import path
path.append('../../modules')

from os import strerror
from debugA import bprint
from math import ceil 

"""
try:
    src = open(input("Source file: "), "r")
except IOError as e:
    print("Couldn't open file: ", strerror(e.errno))
    exit(e.errno)

letters = {}
while (cont := src.read(2000)):
    for char in cont:
        if char.isalpha():
            if char.lower() in letters:
                letters[char.lower()] += 1
            else:
                letters[char.lower()] = 1
"""


try:
    src = open(input("Source file: "), "rb")
except IOError as e:
    print("Couldn't open file: ", strerror(e.errno))
    exit(e.errno)

letters = {}
buffer = bytearray(65536)
readin = src.readinto(buffer)
while readin:
    for b in buffer:
        if chr(b).isalpha() and b < 128:
            if chr(b).lower() in letters:
                letters[chr(b).lower()] += 1
            else:
                letters[chr(b).lower()] = 1
    readin = src.readinto(buffer)


src.close()

max = 0
for i,j in letters.items():
    if j > max:
        max = j
bprint(max)

perced = {}
if max > 100:
    for i,j in letters.items():
        perc = ceil((j/max)*100)
        perced[i] = perc


#Create histogram
def hist(list, dict, chr):
    for item in list:
        if item in dict.keys():
            continue
        else:
            print("dictionary and list do not match")
            return
    display = ""
    for x in list:
        if dict[x] < 100:
            display += x + x.upper() + ' |' + str(dict[x]) + "  |"
        else:
            display += x + x.upper() + ' |' + str(dict[x]) + " |"

        for y in range(dict[x]):
            display += chr
        display += '\n'
    
    return display

#Alphabetical sort
#freq = []
#for i,j in letters.items():
    freq.append(i + i.upper() + " -> " + str(j))

#bprint(freq)
#for x in sorted(freq):
#    print(x)



#print actual histogram
#if perced:
#    print(hist(perced.keys(), perced, '-'))
#else:
#    print(hist(letters.keys(), letters, '-'))

#numerical sort
def freqSort(dict, order = 0):
    num_freq = []
    ct = 0
    for i,j in dict.items():
        bprint(str(i) + ":" + str(j))
        if not len(num_freq):
            bprint("num_freq empty")
            num_freq.append(i)
            bprint(num_freq)
            continue

        if order:
            ct=0
            for x in num_freq:
                #bprint(x + "=" + str(dict[x]))
                if j < dict[x]:
                    bprint(num_freq[ct])
                    num_freq.insert(ct, i)
                    bprint(num_freq[ct])
                    break
                ct+=1
            if ct == len(num_freq):
                num_freq.append(i)
        else:
            ct=0
            for x in num_freq:
                bprint(x + "=" + str(dict[x]))
                if j > dict[x]:
                    num_freq.insert(ct, i)
                    break
                ct+=1
            bprint(ct)
            if ct == len(num_freq):
                num_freq.append(i)

    
    bprint(num_freq)
    return num_freq

if perced:
    print(hist(freqSort(perced, 1), perced, '#'))
else:
    print(hist(freqSort(letters, 1), letters, '#'))
