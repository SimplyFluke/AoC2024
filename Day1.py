with open("input.txt", "r") as f:
    list_one = []
    list_two = []
    difference = 0
    similarity = 0

    for line in f:
        line = line.strip().split()
        list_one.append(int(line[0]))
        list_two.append(int(line[1]))

    list_one = sorted(list_one)
    list_two = sorted(list_two)

    for i in range(len(list_one)):
        difference += abs(list_one[i]-list_two[i])
        similarity += list_one[i] * list_two.count(list_one[i])

    print(f"Difference: {difference}")
    print(f"Similarity Score: {similarity}")
