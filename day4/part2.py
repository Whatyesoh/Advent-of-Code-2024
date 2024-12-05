import re

with open("day4/input.txt","r") as file:
    lines = file.read().split('\n')

sum = 0

xmas = ["M","A","S"]
dirs = [-1,1]

aLoc = []

for i in range(0,len(lines)):
    for j in range(0,len(lines[i])):
        for k in dirs:
            for l in dirs:
                if (i+k < 0 or i+k > len(lines) - 1 or j+l < 0 or j+l > len(lines[i+k]) - 1 or (k == 0 and l == 0 )):
                    continue
                for m in range(0,3):
                    if (i+k * m < 0 or i+k * m > len(lines) - 1 or j+l * m < 0 or j+l * m > len(lines[i+k*m]) - 1):
                        break
                    if (lines[i+k*m][j+l*m]==xmas[m]):
                        if (m == 2):
                            if ([i+k,j+l] in aLoc):
                                sum += 1
                            else:
                                aLoc.append([i+k,j+l])
                        continue
                    break
print(sum)