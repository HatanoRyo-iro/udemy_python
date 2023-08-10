def print_info(func):
    def wrapper(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result
    return wrapper

@print_info  
def add_num(a, b):
    return a + b

# print("start")
# r = add_num(10, 20)
# print("end")
# print(r)


# f = print_info(add_num)
# r = f(10, 20)
# print(r)

r = add_num(10, 20)
print(r)

print("--------------------")

@print_info
def sub_num(a, b):
    return a - b
result = sub_num(10, 20)
print(result)


print("####################")

def print_more(func):
    def wrapper(*args, **kwargs):
        print("func:", func.__name__)
        print("args:", args)
        print("kwargs:", kwargs)
        result = func(*args, **kwargs)
        print("result:", result)
        return result
    return wrapper

@print_info
@print_more
def add_num2(a, b):
    return a + b

r = add_num2(10, 20)
print(r)