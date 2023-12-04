file_path = "./q2.txt"

with open(file_path, "r") as file:
    lines = file.readlines()

total = 0
dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


for line in lines:
    lst = line.split()
    s = []

    for i in lst:
        if i in dict:
            s.append(str(dict[i]))
        else:
            for j in i:
                if j.isdigit():
                    s.append(j)

    if s:
        total += int(s[0] + s[-1])

print("Total =", total)
