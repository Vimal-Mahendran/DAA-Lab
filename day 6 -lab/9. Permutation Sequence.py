import math

def getPermutation(n, k):
    nums = [str(i) for i in range(1, n + 1)]
    result = ""
    k -= 1

    for i in range(n):
        index = k // math.factorial(n - 1 - i)
        result += nums.pop(index)
        k -= index * math.factorial(n - 1 - i)

    return result

n = 3
k = 3
print(getPermutation(n, k))
