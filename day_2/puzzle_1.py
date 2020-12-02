#!/usr/bin/python

num_valid = 0

f = open("input.txt", "r")

for i in range(0, 1000):
    string = f.readline()
    num_occurences = 0
    #Password starts at j + 2
    j = string.index(":")
    #Character we need to find the number of occurences of.
    char = string[j - 1]
    #We can skip the last character, because it's a newline.
    for k in range(j + 2, len(string) - 1):
        if char == string[k]:
            num_occurences += 1

    #Gets our over/under for the number of occurences.
    numbers = string.split(char)[0]
    over = int(numbers.split("-")[0])
    under = int(numbers.split("-")[1])

    if (num_occurences <= under) and (num_occurences >= over):
        num_valid += 1

print(num_valid)
