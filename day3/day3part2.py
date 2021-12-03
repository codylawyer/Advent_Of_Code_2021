import copy

def countBits(values):
    onesCount = [0 for i in range(0,len(values[0]))] 
    zerosCount = [0 for i in range(0,len(values[0]))] 
    for value in values:
        for idx,val in enumerate(value):
            if val == '1':
                onesCount[idx] += 1
            else:
                zerosCount[idx] += 1
    return onesCount,zerosCount

f = open('input.txt')
line = f.readline().strip()

values = []

while line:
    values.append(line)
    line = f.readline().strip()

onesCount,zerosCount = countBits(values)

oxygen = '0'
co2  = '0'

oxygenValues = copy.deepcopy(values)
co2Values = copy.deepcopy(values)

for idx in range(len(onesCount)):
    onesCount,zerosCount = countBits(oxygenValues)
    if len(oxygenValues) > 1:
        if onesCount[idx] > zerosCount[idx]:
            valueToKeep = '1'
        elif onesCount[idx] == zerosCount[idx]:
            valueToKeep = '1'
        else:
            valueToKeep = '0'
        valuesToKeep = []
        for value in oxygenValues:
            if value[idx]==valueToKeep:
                valuesToKeep.append(value)
        oxygenValues = valuesToKeep
oxygen = oxygenValues[0]

for idx in range(len(onesCount)):
    onesCount,zerosCount = countBits(co2Values)
    if len(co2Values) > 1:
        if onesCount[idx] < zerosCount[idx]:
            valueToKeep = '1'
        elif onesCount[idx] == zerosCount[idx]:
            valueToKeep = '0'
        else:
            valueToKeep = '0'
        valuesToKeep = []
        for value in co2Values:
            if value[idx]==valueToKeep:
                valuesToKeep.append(value)
        co2Values = valuesToKeep
co2 = co2Values[0]

oxygen = int(oxygen,2)
co2 = int(co2,2)
print(oxygen*co2)
