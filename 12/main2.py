


d = "..##...##...##...##...##...##...##...##...##...##...##...##...##...##...##...##...##...##...##...##...##...##...##...##...##...##...##...##...##...##...##...##...##...##...##...##...##...##...##...##"

val = 0
for i in range(0, len(d)):
    if d[i] == "#":
        val += i + (50000000000 - 100)

print(val)