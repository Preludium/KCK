l = []
with open('dane.txt', 'r') as f:
    f.readline()
    for line in f:
        for item in line.split():
            l.append(float(item) / 100)

print(min(l))