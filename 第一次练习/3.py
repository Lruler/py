nums = [1,2,3,4,5,6,7,8,9,10]
sum = 0

for x in nums:
    i = 1
    k = 1
    while (i <= x):
        k *= i
        i += 1
    sum += k


print(sum)
    