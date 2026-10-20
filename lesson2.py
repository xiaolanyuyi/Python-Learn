def listtest():
    nums = [1, 2, 3, 4, 5]
    mixed = [1, "hello", True, None]

    print(nums[0], nums[-1])
    print(len(nums), len(mixed))
    print(5 in nums, 6 in nums)
    print(nums + [6, 7])
    print([0] * 3)

def test():
    for item in [10, 20, 30]:
        print(item)

    for i, v in enumerate(["a", "b"]):  # 需要下标用 enumerate
        print(i, v)

    for k, v in {"x": 1}.items():  # 遍历字典
        print(k, v)

    for i in range(3):  # 0 1 2
        print(i)

def lesson2():
    nums = [1, 2, 3, 4, 5]
    print(max(nums), min(nums), sum(nums), sum(nums)/len(nums))

    words = ["apple", "banana"]
    words.append("cherry")
    words.insert(1, "orange")
    words.remove("banana")
    words.sort()
    print(words)

    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(nums[:3]) # 0, 1, 2
    print(nums[-3:]) # 7, 8, 9
    print(nums[2:6]) # 2, 3, 4, 5
    print(nums[::2]) # 0, 2, 4, 6, 8
    print(nums[::-1]) # 9, 8, 7, ... , 2, 1, 0

    text = input("Enter a sentence: ")
    counts = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    print(counts)

    nums = [3, 1, 2, 3, 1, 5]
    nums = list(set(nums))
    print(nums, len(nums))

    print({"a": 1, "b": 2} | {"b": 9, "c": 3})

    # a = [1, 2, 3]; b = a; b.append(4) 后 print(a) 输出什么？为什么？
    # 1, 2, 3, 4 因为a, b是同一个列表

    # s = {} 是什么类型？空集合怎么创建？
    # 是空字典 set()

def main():
    lesson2()

if __name__ == "__main__":
    main()
