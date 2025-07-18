from itertools import combinations

N = int(input())
S = [list(map(int, input().split())) for i in range(N)]

team_combinations = combinations(range(N), N//2)

def team_ability(team, S):
    ability = 0

    for i in range(len(team)):
        for j in range(i+1, len(team)):
            ability += S[team[i]][team[j]] + S[team[j]][team[i]]

    return ability

min_diff = float('inf')

for start in team_combinations:
    link = list(set(range(N)) - set(start))
    diff = abs(team_ability(start, S) - team_ability(link, S))
    min_diff = min(min_diff, diff)

print(min_diff)