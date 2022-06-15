#!/usr/bin/python3.9
from sys import argv

def sort(list):
    while True:
        good = True
        for i in range(len(list)-1):
            if list[i] > list [i+1]:
                good = False
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
        if good:
            break
    return list

def solve(coins, total):
    try:
        i = len(coins)-1
        while total:
            if coins[i] > total:
                i-=1
                continue
            result.append(coins[i])
            total-=coins[i]
    except:
        result = 0
        print("No solutions found!")
    return result


coins = []
total = 0
result = []

if len(argv) > 1:
    #command-line args
    args = ""
    i=1
    for i in range(1,len(argv)):
        if argv[i] == "-c":
            args = "c"
            continue
        if argv[i] == "-t":
            args = "t"
            continue
        if args == "c":
            coins.append(int(argv[i]))
        if args == "t":
            total = int(argv[i])
    coins = sort(coins)
else:
    #text interface
    while True:
        value = input("Add a coin value, or minus when done: ")
        if value == "-": break
        if value == "0": continue
        try: coins.append(int(value))
        except: value = input("Please input a numerical value: ")
    coins = sort(coins)
    print(f"Your coins are {coins}")
    value = input("Add an amount to add up to: ")
    while True:
        try:
            total = int(value)
            break
        except: value = input("Please input a numerical value: ")

solve(coins, total)
print(result)