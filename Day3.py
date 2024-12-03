import re

part1_result = 0
part2_result = 0

with open("input.txt", "r") as f:
    file = f.read()
    instructions = re.findall("mul\(\d+,\d+\)", file)

    for i in range(len(instructions)):
        digits = re.findall("\d+", instructions[i])
        part1_result += (int(digits[0]) * int(digits[1]))

    instructions = file.strip().replace("\n", "")
    instructions = re.sub("(don\'t\(\)).+?(do\(\))", "", instructions)
    instructions = re.sub("(don\'t\(\)).+", "", instructions)
    instructions = re.findall("mul\(\d+,\d+\)", instructions)

    for i in range(len(instructions)):
        digits = re.findall("\d+", instructions[i])
        part2_result += (int(digits[0]) * int(digits[1]))

    print(f"Part 1: {part1_result}")
    print(f"Part 2: {part2_result}")
