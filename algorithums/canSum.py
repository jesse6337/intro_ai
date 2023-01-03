def canSum(target, numbers, tested = {}):
    if target in tested: return tested[target]
    if target == 0: return True
    if target < min(numbers): return False
    for i in numbers:
        remainder = target-i
        if canSum(remainder, numbers, tested) == True: return True
        else: tested[target] = False
    return False
print(canSum(9008, (14,87)))
