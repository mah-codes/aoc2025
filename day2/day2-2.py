with open("input.txt", "r") as input_file:
    input_data = input_file.readlines()

output = []

# parse the intervals from the string'd list (remove final \n)
input_str = input_data[0]
intervals = input_str.split(",")

# loop through the interval, with at least 2 digits repeated
for interval in intervals:
    start, end = map(int, interval.split("-"))
    for num in range(start, end + 1):
        tgt = ""
        half = int(len(str(num)) / 2)
        for char in str(num)[:half]:
            tgt += char
            # if len(tgt) < 2:
                # continue
            if not any(str(num).split(tgt)):
                output.append(num)
# remove duplicates
output = set(output)

print("="*10, "FINAL Answer","="*10)
print(output)
print(sum(output))
