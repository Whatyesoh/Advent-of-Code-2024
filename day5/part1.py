import re

with open("day5/input.txt","r") as file:
    lines = file.read().split('\n')

rules = {}
orders = []

for line in lines:
    if (re.search("\|",line) != None):
        ruleNums = re.findall("\d+",line)
        if (ruleNums[0] in rules):
            rules[ruleNums[0]].append(ruleNums[1])
        else:
            rules[ruleNums[0]] = [(ruleNums[1])]
    elif (re.search(",",line) != None):
        orders.append(line)

sum = 0

for order in orders:
    works = 1
    nums = []
    middle = 0
    allNums = re.findall("\d+",order)
    for i in range(0,len(allNums)):
        number = allNums[i]
        if (number in rules):
            for rule in rules[number]:
                if (rule in nums):
                    works = 0
        nums.append(number)
    if (works == 1):
        sum += int(allNums[int(len(allNums)/2)])
    
print(sum)