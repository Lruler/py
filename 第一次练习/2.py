num = input()

numList = []

def decomposition(num):
    i = 2
    if(num == 1 | num == 2 | num == 3):
        numList.append(num)
        return numList
    while(i <= num / 2):
        if(num % i == 0):
            numList.append(i)
            decomposition(num / i)
            break
        i += 1
    if(i > num / 2):
        numList.append(num)
    return numList


decomposition(num)

print(numList)