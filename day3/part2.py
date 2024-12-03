import re

with open("day3/input.txt","r") as file:
    wholeText = file.read()

sum = 0

muls = []
dos = []
donts = []
for mul in re.finditer("mul\(\d+,\d+\)",wholeText):
    muls.append([mul.start(),mul.group()])

for do in re.finditer("do\(\)",wholeText):
    dos.append(do.start())

for dont in re.finditer("don't\(\)",wholeText):
    donts.append(dont.start())

for mul in muls:
    latestDo = 0
    latestDont = -1
    for do in dos:
        if (do > latestDo and do < mul[0]):
            latestDo = do
    for dont in donts:
        if (dont > latestDont and dont < mul[0]):
            latestDont = dont

    if (latestDo > latestDont):
        nums = re.findall("\d+",mul[1])
        sum += int(nums[0]) * int(nums[1])
    
print(sum)