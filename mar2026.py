n, m = map(int, input().split())

g = [[0]*n for x in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    a-= 1; b -=1 
    g[a][b] = g[b][a] = 1

ew = [0] * (1 << n)
for mk in range(1, 1 << n):
    v = (mk & -mk).bit_length() - 1
    r = mk ^ (1 << v)
    ew[mk] = ew[r] + sum(g[v][u] for u in range(n) if r >> u & 1)

dp = [float('inf')] * (1 << n)
dp[0] = 0 

for mk in range(1, 1<<n):
    s = mk 
    while s:
        k = bin(s).count('1')
        val = dp[mk ^ s] + 2*ew[s] - k*(k-1)//2 
        if val < dp[mk]: dp[mk] = val
        s = (s-1) & mk 

ops = dp[(1<<n)-1] + n*(n-1)//2 - m 
print(max(0, 100-ops))

