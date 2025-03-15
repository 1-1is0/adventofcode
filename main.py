group1, group2 = [], []

with open("data.txt", "r") as file:
    for line in file.readlines():
        one, two = line.strip().split()
        group1.append(int(one))
        group2.append(int(two))

group1.sort()
group2.sort()

s = 0
for one, two in zip(group1, group2):
    s += abs(one - two)
print("total distance: ", s)
