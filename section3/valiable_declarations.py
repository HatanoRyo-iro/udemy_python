num: int = 1   # 型の宣言もできるが，違くてもエラーにならない
name: str = '1'

new_num = int(name)

print(new_num, type(new_num))