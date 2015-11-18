__author__ = 'navin.kolambkar'

# https://www.hackerrank.com/challenges/play-game/editorial
def get_max_score():
    N = 5
    # 999 is bottom of stack
    bricks = [999, 1, 1, 1, 0]
    bricks = [0] + bricks
    sum = [0] * (N+1)
    # max score with i as top of stack
    dp = [0] * (N+1)
    total = 0

    for i in range(1, N+1):
        sum[i] = sum[i-1] + bricks[i]

    dp[0] = 0
    dp[1] = bricks[0]
    dp[2] = bricks[0] + bricks[1]
    dp[3] = bricks[0] + bricks[1] + bricks[2]

    for i in range (4, N+1):
        # I take ith brick
        m1 = sum[i-1] - dp[i-1] + bricks[i]
        m2 = sum[i-2] - dp[i-2] + bricks[i] + bricks[i-1]
        m3 = sum[i-3] - dp[i-3] + bricks[i] + bricks[i-1] + bricks[i-2]
        dp[i] = max(m1, m2, m3)

    print dp[N]

# Not quite working
get_max_score()