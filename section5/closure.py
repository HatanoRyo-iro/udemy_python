def outer(a, b):
    
    def inner():
        return a + b
    
    return inner

f = outer(1, 2)   # この時点ではfにはinnerが代入されている
r = f()           # この時点でinner関数が実行されている
print(r)      # 3


# クロージャーはどんな時に使うのか？
"""
f = outer(1, 2)
ここでキープしておいて、まだ実行したくない時に使うとか
"""

print("####################")

def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius
    
    return circle_area

cal1 = circle_area_func(3.14)
cal2 = circle_area_func(3.141592)

print(cal1(10))
print(cal2(10))
