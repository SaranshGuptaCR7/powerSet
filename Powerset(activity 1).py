import math
def printPowerset(set, setSize):
    powSetSize = math.pow(2, setSize)
    for i in range(0, int(powSetSize)):
        for j in range(0, setSize):
            if (i & (1 << j)) > 0:
                print(set[j], end="")
        print("")
size = int(input("Enter size of set: "))
set = []
for i in range(0, size):
    n = input("Enter element: ")
    set.append(n)
    printPowerset(set, len(set))