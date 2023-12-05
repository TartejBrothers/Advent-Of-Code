file_path = "./q2.txt"
index = 1
numr = 0
numg = 0
numb = 0
total = 0
with open(file_path, "r") as file:
    data = file.read().strip()
print(data)
