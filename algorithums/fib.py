import time
def fib(n, memo = {}):
    if n in memo: return memo[n]
    if n <= 2: return 1
    memo[n] = (fib(n-1, memo)+fib(n-2, memo))
    return memo[n]
start = time.time()
print(fib(791))
end = time.time()-start
print(end)
def badFib(n):
    if n <= 2: return 1
    return badFib(n-1)+badFib(n-2)
start = time.time()
print(badFib(40))
end = time.time()-start
print(end)
