# To use to flatten lists
def flatten(lst):
    for item in lst:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

with open('input.txt', 'r') as file:
    lines = file.readlines()

lines = [line[:-1] for line in lines]

start = 50
traversal = []
for line in lines:
    if line[0] == "R":
        sub_trav = [(start + item) % 100 for item in range(int(line[1:]))]
        start += int(line[1:]) % 100
    else:
        sub_trav = [(start - item) % 100 for item in range(int(line[1:]))]
        start -= int(line[1:]) % 100
    traversal.append(sub_trav)
    
# Flatten lists (1 depth)
flat_traversal = list(flatten(traversal))
print(flat_traversal)

# count number of 0's in traversal:
zeros = [item for item in flat_traversal if item == 0]
print(zeros)
print(f"num of zero's = {len(zeros)}")
