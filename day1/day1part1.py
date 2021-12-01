f = open('input.txt')
line = f.readline()

nums = []

while line:
    nums.append(int(line.strip()))
    line = f.readline()

increasing = 0
for i in range(1,len(nums)):
    if nums[i]-nums[i-1]>0:
        increasing += 1

print(increasing)
