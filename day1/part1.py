import re

with open("day1/input.txt","r") as file:
    lines = file.read().split('\n')

left = []
right = []

for line in lines:
    nums = re.findall("\d+",line)
    left.append(int(nums[0]))
    right.append(int(nums[1]))

left.sort()
right.sort()

sum = 0

for i in range(0,len(left)):
    sum += abs(left[i] - right[i])

print(sum)