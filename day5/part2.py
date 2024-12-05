import re
from functools import cmp_to_key

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

def compare(left,right):
    if (left in rules):
        for rule in rules[left]:
            if (rule == right):
                return -1
    if (right in rules):
        for rule in rules[right]:
            if (rule == left):
                return 1
    return 0

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
    if (works == 0):
        sortedOrder = sorted(allNums, key=cmp_to_key(compare))
        sum += int(sortedOrder[int(len(sortedOrder)/2)])
    
print(sum)