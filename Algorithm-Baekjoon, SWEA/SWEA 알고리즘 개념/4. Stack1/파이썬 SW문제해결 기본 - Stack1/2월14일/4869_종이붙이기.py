T = int(input())

for t in range(T):
    N = int(input())//10

    dp = [0 for x in range(N)]
    dp[0] = 1
    dp[1] = 3

    for i in range(2,len(dp)):
        dp[i] = dp[i-1] + dp[i-2]*2
    
    print(f"#{t+1} {dp[N-1]}")