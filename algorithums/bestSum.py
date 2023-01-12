def bestSum(target,numbers, howlist= [], memo = {}):
    if target == 0: return []
    if target< min(numbers): return None
    for i in sorted(numbers, reverse= True):
        remainder = target-i
        memo[remainder] = bestSum(remainder, numbers, howlist, memo)
        if memo[remainder] != None:
            howlist.append(i)
            return howlist
total  = bestSum(100, [1,2,5,25])
print(total, sum(total), len(total))