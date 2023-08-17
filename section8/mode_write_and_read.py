# 書き込みと読み込みの両方をやりたい場合

s = """\
AAA
BBB
CCC
DDD
"""

# # 書き込んで、読み込みOK
# with open('section8/test.txt', 'w+') as f:
#     f.write(s)  # 書き込んだ後は一番最後のインデックスにいる
#     f.seek(0)   # -> 書き込んだ後に、一番最初戻らないといけないため、f.seek(0)が必要になる
#     print(f.read())
    
    
    
# 読み込んで、書き込みOK
"""
読み込むものがないとエラーになる
"""
with open('section8/test.txt', 'r+') as f:
    print(f.read())
    f.seek(0)
    f.write(s)