from copy import copy
from hmac import new


nums = [1,2,3,4]
ns = []

for x in nums:
    a = copy(nums)
    a.remove(x)
    x = x*100
    for y in a:
        b = copy(a)
        b.remove(y)
        y = y*10
        for j in b:
            ns.append(x + y + j)

print(sorted(ns), len(ns))