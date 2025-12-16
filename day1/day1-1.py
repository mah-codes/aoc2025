with open('input.txt', 'r') as file:
    lines = file.readlines()

lines = [line[:-1] for line in lines]

start = 50
counter = 0
for line in lines:
    if line[0] == "R":
        start += int(line[1:])
    else:
        start -= int(line[1:])
    start = start % 100
    if start == 0:
        counter += 1
print(counter)

