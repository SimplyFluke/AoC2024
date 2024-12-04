import re
import numpy as np

def findXmas(collection):
    horizontal = []
    checked = []
    found = 0
    for i in range(len(collection)):
        horizontal.append("".join(str(letter) for letter in collection[i]))

    for item in horizontal:
        found += len(re.findall("XMAS", item))
        found += len(re.findall("SAMX", item))
    
    for i in range(len(collection)-3):
        check = np.diag(collection, k=i)
        string = "".join(str(letter)for letter in check)
        if string not in checked:
            found += len(re.findall("XMAS", string))
            found += len(re.findall("SAMX", string))
            checked.append(string)

    for i in range(len(collection)-3):
        check = np.diag(collection, k=-i)
        string = "".join(str(letter)for letter in check)
        if string not in checked:
            found += len(re.findall("XMAS", string))
            found += len(re.findall("SAMX", string))
            checked.append(string)

    rotated = list(zip(*collection))[::-1]
    horizontal = []
    
    for i in range(len(rotated)):
        horizontal.append("".join(str(letter) for letter in rotated[i]))

    for item in horizontal:
        found += len(re.findall("XMAS", item))
        found += len(re.findall("SAMX", item))
    
    for i in range(len(rotated)-3):
        check = np.diag(rotated, k=i)
        string = "".join(str(letter)for letter in check)
        if string not in checked:
            found += len(re.findall("XMAS", string))
            found += len(re.findall("SAMX", string))
            checked.append(string)

    for i in range(len(rotated)-3):
        check = np.diag(rotated, k=-i)
        string = "".join(str(letter)for letter in check)
        if string not in checked:
            found += len(re.findall("XMAS", string))
            found += len(re.findall("SAMX", string))
            checked.append(string)
    
    return found


def findMAS(collection):
    count = 0
    done = []

    for y in range(len(collection)-1):
        for x in range(len(collection[y])-1):
            if collection[y][x] == "A" and x > 0 and y > 0:
                try:
                    found = ["A"]
                    found.append(collection[y-1][x-1])
                    found.append(collection[y-1][x+1])
                    found.append(collection[y+1][x-1])
                    found.append(collection[y+1][x+1])

                    if sorted(found) == ['A', 'M', 'M', 'S', 'S'] and f"{y}:{x}" not in done and found[1] != found[4] and found[3] != found[2]:
                        count += 1
                        done.append(f"{y}:{x}")
    
                except:
                    pass
    
    return count


with open("input.txt", "r") as f:
    collection = []

    for line in f:
        line = line.strip()
        collection.append(list(line))

    print(f"Part 1: {findXmas(collection)}")
    print(f"Part 2: {findMAS(collection)}")
