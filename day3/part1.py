import re

with open("day3/input.txt","r") as file:
    lines = file.read().split('\n')

sum = 0

for line in lines:
    muls = re.findall("mul\(\d+,\d+\)",line)
    for mul in muls:
        nums = re.findall("\d+",mul)
        sum += int(nums[0]) * int(nums[1])
    
print(sum)