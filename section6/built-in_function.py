import builtins


print(globals())

print('------------------')

ranking = {
    'A': 100,
    'B': 85,
    'C': 95
}

# for k, v in ranking.items():
#     print(k, v)
    

print(sorted(ranking, key=ranking.get, reverse=True))