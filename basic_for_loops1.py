# 1
for x in range(150 + 1):
    print(x)
print("-"*50)
# 2
for x in range(5, 1000 + 1, 5):
    print(x)
print("-"*50)
# 3
for x in range(1, 100 + 1):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)
print("-"*50)
# 4
x = 0
for i in range(0, 500_000 + 1):
    x += i
print(x)
print("-"*50)
# 5
lowNum = 2
highNum = 9
mult = 3
for x in range(lowNum, highNum + 1):
    if x % mult == 0:
        print(x)
print("-"*50)
