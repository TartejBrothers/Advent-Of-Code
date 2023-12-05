file_path = "./q1.txt"
index = 1
numr = 0
numg = 0
numb = 0
total = 0
with open(file_path, "r") as file:
    data = file.read().strip()
for line in data.split("\n"):
    line = line.split(":")[1]
    print("Index =", index)
    print("Total =", total)
    for event in line.split(";"):
        for time in event.split(","):
            time = time.split(" ")
            if time[2] == "red":
                numr += int(time[1])
            elif time[2] == "green":
                numg += int(time[1])
            elif time[2] == "blue":
                numb += int(time[1])
    print("numr =", numr)
    print("numg =", numg)
    print("numb =", numb)
    if numb <= 14 and numg <= 13 and numr <= 12:
        print("Added Index =", index)
        total += int(index)
    numr = 0
    numg = 0
    numb = 0
    index += 1
    print("=" * 80)
print(total)
