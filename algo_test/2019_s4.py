import math
upmost_visiting = 3
cities_num = 5
attaction = [2,5,7,1,4]

dp = [0 for _ in range(cities_num-1)]
dp[0] = attaction[0]


for i in range(1,cities_num):
    minimum_days = math.ceil(i / upmost_visiting)
    if minimum_days == 1:
        dp[i] = max(dp[i-1],attaction[i])
    else:



