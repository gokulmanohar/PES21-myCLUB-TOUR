val = []
try:
    with open("val.txt", mode="r") as target:
        for line in target:
            if line == "\n":
                continue
            else:
                val.append(float(line))
except:
    with open("internal\testing\val.txt", mode="r") as target:
        for line in target:
            if line == "\n":
                continue
            else:
                val.append(float(line))
print(sum(val))
