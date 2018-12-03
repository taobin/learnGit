from functools import reduce
def f(x):
    return x*x
r = map(f,[1,2,3,4,5,6,7,8,9])
mm =list(r)
print(mm)


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]
map2=map(char2num,'13579')
for n in map2:
    print(n)

def fn(x, y):
    return x * 10 + y

reduce2 =reduce(fn,map(char2num,'13579'))
print(reduce2)
