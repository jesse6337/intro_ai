def howSum(target, numbers, howlist = [], memo = {}):
    #if target in memo:return memo[target]
    if target == 0:
        return howlist
    if target < 0:
        return None
    for i in numbers:
        #print(target)
        remainder = target - i
        print(remainder)
        check = howSum(remainder, numbers, howlist)
        howlist.append(i)
        if check != None: return howlist
        
        
print(howSum(49, [14,7]))