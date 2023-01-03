def gridTravel (m,n):
    if m == 1 and n ==1: return 1
    if m == 0 or n ==0: return 0
    return gridTravel(m-1,n)+ gridTravel(m,n-1)
print(gridTravel(10,10))

def goodGridTravel (m,n, memo ={}):
    key = '{}, {}'.format(m,n)
    if key in memo.keys(): return memo[key]
    if m == 1 and n ==1: return 1
    if m == 0 or n ==0: return 0
    memo[key] = goodGridTravel(m-1,n,memo)+ goodGridTravel(m,n-1,memo)
    return memo[key]
print(goodGridTravel(10,10))

