parts = input().split('-')
result = 0

# Calculate the sum of the first part (before the first '-')
first_part_numbers = parts[0].split('+')
for num_str in first_part_numbers:
    result += int(num_str)

# Subtract the sums of all subsequent parts
for part in parts[1:]:
    sub_part_numbers = part.split('+')
    part_sum = 0
    for num_str in sub_part_numbers:
        part_sum += int(num_str)
    result -= part_sum

print(result)