memo = [0] * 100
memo[0] = 0
memo[1] = 1
def f(n):
    if n <2 or memo[n] != 0 :
        return memo[n]
    memo[n] = f(n-1) + f(n-2)
    return memo[n]

print(f(5))