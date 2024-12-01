import re

with open("day1/input.txt","r") as file:
    lines = file.read().split('\n')

left = []
right = {}

for line in lines:
    nums = re.findall("\d+",line)
    left.append(int(nums[0]))
    right[int(nums[1])] = right.get(int(nums[1]), 0) + 1

sum = 0

for i in left:
    if (i in right):
        sum += i * right[i]

print(sum)