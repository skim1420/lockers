lockers = {}
# userInput = raw_input('How many lockers?: ')
# numLockers = int(userInput)
numLockers = 100



# Method 1: brute force

print('\nMethod 1: brute force\n')

def lockersToString():
    lockersString = ''
    for i in range(1, numLockers + 1):
        lockersString += str(lockers[i])
    return lockersString

def flipLockers(num):
    for i in range(1, numLockers + 1):
        if i % num == 0:
            if lockers[i] == 0:
                lockers[i] = 1
            else:
                lockers[i] = 0

for i in range(1, numLockers + 1):
    lockers[i] = 0
print(lockersToString() + ' : 0')

for i in range(1, numLockers + 1):
    flipLockers(i)
    print(lockersToString() + ' : ' + str(i))

bruteAnswer = []
for i in range(1, numLockers + 1):
    if lockers[i] == 1:
        bruteAnswer.append(i)
print bruteAnswer



# Method 2: odd number of factors

print('\nMethod 2: odd number of factors\n')

evenFactorAnswer = []
for i in range(1, numLockers +1):
    factorsPrint = ''
    numFactors = 0
    for j in range(1, i + 1):
        if i % j == 0:
            numFactors += 1
            factorsPrint += str(j).rjust(2, '-')
        else:
            factorsPrint += '--'
    if numFactors % 2 != 0:
        evenFactorAnswer.append(i)
    print factorsPrint
print evenFactorAnswer
