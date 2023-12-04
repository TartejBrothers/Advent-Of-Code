file_path = "./q1.txt"
with open(file_path, "r") as file:
    data = file.read()
s = 0
total = 0
lst = list(data.split("\n"))
for i in lst:
    s = 0
    for j in range(0, len(i)):
        if i[j].isdigit():
            s += int(i[j])
            s = s * 10
            break
    for j in range(len(i) - 1, -1, -1):
        if i[j].isdigit():
            s += int(i[j])
            break
    total = total + s
print("Total =", total)
