from traceback import print_tb


def variabletype():
    x = 1.5
    print(type(x))
    x = 2
    print(type(x))

    print(type(x+1.5))

    x = 'hello'
    print(type(x))

def division():
    print(1/3)
    print(3/2)
    print(4/2)
    print(4.0/2)
    print(4//0.5)
    print(7//3)
    print(2 ** 10)
    print(9 % 3)
    print(9 % 2)
    print(None)

def stringtest():
    name, age = "Peter", 20
    print(f"{name} is {age} years old, next year {age + 1} years old")

    s = "  hello world  "
    print(s)
    print(s.split())
    print(s.strip().split())
    print("-".join(["a", "b", "c"]))
    print(len(s))

def printandinput():
    print("a", 1, True)
    x = input("Enter number: ")
    print(x, type(x))
    x = int (x)
    print(x, type(x))

def lesson1():
    name = "Peter"
    age = 20

    print(f"我是{name},今年{age}岁")

    x = input("Enter number: ")
    x = int(x)
    print(x ** 2)

    print(7/2, type(7/2))
    print(7//2, type(7//2))
    print(7%2, type(7%2))
    print(2 ** 10, type(2 ** 10))
    print(7.0//2, type(7.0//2))

    x = input("Enter a sentence: ")
    print(" ".join(x.split()[::-1]))

    x = input("Enter a Celsius: ")
    print(float(x) * 1.8 + 32)

    # 思考题：0.1 + 0.2 == 0.3 是什么结果？为什么？
    # false 因为这几个小数在二进制里都是无限小数 会有误差
