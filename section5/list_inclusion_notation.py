t = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8, 9, 10)

r = []
for i in t:
    if i % 2 == 0:
        r.append(i)
    
print(r)

r = [i for i in t if i % 2 == 0]
print(r)
r2 = [i if i % 2 == 0 else 'odd' for i in t]
print(r2)

r = []
for i in t:
    for j in t2:
        r.append(i * j)

print(r)

r = [i*j for i in t for j in t2]
print(r)


print('####################')

numbers = [1, 2, 3, 4, 5]
result = [x if x % 2 == 0 else "odd" for x in numbers]
print(result)  # [odd, 2, odd, 4, odd]