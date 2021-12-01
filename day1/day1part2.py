f = open('input.txt')
line = f.readline()

nums = []

while line:
    nums.append(int(line.strip()))
    line = f.readline()

increasing = 0
for i in range(3,len(nums)):
    #print(sum(nums[i-3:i]))
    if sum(nums[i-2:i+1])-sum(nums[i-3:i])>0:
        increasing += 1

#print(sum(nums[i-2:i+1]))
print(increasing)
