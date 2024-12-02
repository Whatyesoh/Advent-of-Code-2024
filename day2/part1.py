import re

with open("day2/input.txt","r") as file:
    lines = file.read().split('\n')

sum = 0

for line in lines:
    nums = re.findall("\d+",line)
    dir = 0
    safe = 1
    for i in range(1,len(nums)):
        if (int(nums[i]) < int(nums[i-1])):
            if (dir == 1):
                safe = 0
                break
            dir = -1
        elif (int(nums[i]) > int(nums[i-1])):
            if (dir == -1):
                safe = 0
                break
            dir = 1
        else:
            safe = 0
            break
        if (abs(int(nums[i])-int(nums[i-1])) > 3):
            safe = 0
            break
    sum += safe
print(sum)