file_path = "./q2.txt"
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
                if numr < int(time[1]):
                    numr = int(time[1])
            elif time[2] == "green":
                if numg < int(time[1]):
                    numg = int(time[1])
            elif time[2] == "blue":
                if numb < int(time[1]):
                    numb = int(time[1])
    print("numr =", numr)
    print("numg =", numg)
    print("numb =", numb)

    mul = 0
    mul = numr * numg * numb
    print("mul =", mul)
    total += mul
    numr = 0
    numg = 0
    numb = 0
    index += 1
    print("=" * 80)
print(total)
