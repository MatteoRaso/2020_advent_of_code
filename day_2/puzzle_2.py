#!/usr/bin/python

num_valid = 0

f = open("input.txt", "r")

for i in range(0, 1000):
    string = f.readline()
    j = string.index(":")
    char = string[j - 1]
    numbers = string.split(char)[0]
    #We have to subtract by 1 because elves are heathens who don't index at zero.
    first = int(numbers.split("-")[0]) - 1
    second = int(numbers.split("-")[1]) - 1

    password = string[(j + 2):]
    if (password[first] == char and password[second] != char) or (password[second] == char and password[first] != char):
        num_valid += 1

print(num_valid)
