def climbingLeaderboard(ranked, player):
    ranked = sorted(set(ranked), reverse=True)
    n = len(ranked)
    result = []

    for score in player:
        while n > 0 and score >= ranked[n - 1]:
            n -= 1
        result.append(n + 1)
    return result


ranked = list(map(int,input().split()))
player = list(map(int,input().split()))
print(climbingLeaderboard(ranked, player))