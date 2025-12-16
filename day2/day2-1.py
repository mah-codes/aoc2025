with open("input.txt", "r") as input_file:
    input_data = input_file.readlines()

output = []

# parse the intervals from the string'd list (remove final \n)
input_str = input_data[0]
intervals = input_str.split(",")

# loop through the interval, considering half of number of digits (decimal) of current iterant
for interval in intervals:
    start, end = map(int, interval.split("-"))
    for num in range(start, end + 1):
        if len(str(num)) % 2 != 0:
            continue
        half = int(len(str(num)) / 2)
        # if number consists of duplicated sequence, add to output list
        if str(num)[:half] == str(num)[half:]:
            output.append(num)

print("="*10, "FINAL Answer","="*10)
print(output)
print(sum(output))
