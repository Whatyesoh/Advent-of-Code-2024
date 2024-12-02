import re

with open("day2/input.txt","r") as file:
    lines = file.read().split('\n')

sum = 0

def checkSafe(nums):
    safe = 1
    dir = 0
    increaseNum = 0
    decreaseNum = 0
    for i in range(1,len(nums)):
        if (int(nums[i]) < int(nums[i-1])):
            decreaseNum += 1
        elif (int(nums[i]) > int(nums[i-1])):
            increaseNum += 1
        else:
            safe = 0
            break
        if (abs(int(nums[i])-int(nums[i-1])) > 3):
            safe = 0
            break
    if (increaseNum > 0 and decreaseNum > 0):
        safe = 0
    return safe
            

for line in lines:
    nums = re.findall("\d+",line)
    for i in range(0,len(nums)):
        nums[i] = int(nums[i])
    safe = checkSafe(nums)
    newSafe = 0
    if (safe == 0):
        newSafe = 0
        for i, num in enumerate(nums):
            newNums = nums[:i] + nums[i + 1 :]
            newSafe += checkSafe(newNums)
        if (newSafe >= 1):
            sum += 1
    else:
        sum += 1

print(sum)