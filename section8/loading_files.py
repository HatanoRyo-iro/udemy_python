s = """\
AAA
BBB
CCC
DDD
"""
# with open('section8/test.txt', 'w') as f:
#     f.write(s)

with open('section8/test.txt', 'r') as f:
    #print(f.read())
    while True:
        chunk = 2
        line = f.read(chunk)
        print(line)
        if not line:
            break