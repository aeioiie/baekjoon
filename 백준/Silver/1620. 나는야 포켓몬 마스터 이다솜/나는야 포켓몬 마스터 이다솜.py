N, M = map(int, input().split())
pokemons = {}
index = {}

# for i in range(N):
#     pokemon = input()
#     pokemons[pokemon] = i+1

# for i in range(M):
#     q = input()
#     if q.isdigit():
#         print(list(pokemons.keys())[int(q)-1])
#     else:
#         print(pokemons[q])

# 이러면 리스트 때문에 시간 초과

for i in range(N):
    pokemon = input()
    pokemons[pokemon] = i+1
    index[i+1] = pokemon

for i in range(M):
    q = input()
    if q.isdigit():
        print(index[int(q)])
    else:
        print(pokemons[q])