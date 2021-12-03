f = open('input.txt')
line = f.readline().strip()

onesCount = [0 for i in range(0,len(line))] 
zerosCount = [0 for i in range(0,len(line))] 

while line:
    for idx,val in enumerate(line):
        if val == '1':
            onesCount[idx] += 1
        else:
            zerosCount[idx] += 1
    line = f.readline().strip()

gamma = ''
epsilon = ''

for idx in range(len(onesCount)):
    if onesCount[idx] > zerosCount[idx]:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

gamma = int(gamma,2)
epsilon = int(epsilon,2)
print(gamma*epsilon)
