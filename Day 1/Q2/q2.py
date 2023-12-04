file_path = "./q2.txt"
with open(file_path, "r") as file:
    lst = file.readlines()

total = 0
dict = {
    "zero": 0,
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


for i in lst:
    s = []
    for j in range(0, len(i)):
        if i[j].isdigit():
            s.append(i[j])
        else:
            for n in range(j + 1, len(i)):
                if i[j:n] in dict:
                    s.append(str(dict[i[j:n]]))
    total += int(s[0] + s[-1])
print("Total =", total)
