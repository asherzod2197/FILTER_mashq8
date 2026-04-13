# 36-40
roy = ["abc", "xyz"]
print(list(filter(lambda x: "x" in x, roy)))

roy = [14, 28, 42]
print(list(filter(lambda x: x > 20, roy)))

roy = ["one", "four", "six"]
print(list(filter(lambda x: len(x) == 3, roy)))

roy = [5, 15, 25]
print(list(filter(lambda x: x < 20, roy)))

roy = ["hello", "hi"]
print(list(filter(lambda x: len(x) > 2, roy)))
