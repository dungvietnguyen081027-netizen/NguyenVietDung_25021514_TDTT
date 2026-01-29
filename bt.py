a, b, c = map(int, input().split())
max_num = i if a > b and a > c else (b if b > c else c)
print(max_num)