#方法一
def normalize(name):
    return name.capitalize()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#方法二
def normalize2(s):
    return s[0].upper() + s[1:].lower()
 
L3 = ['adadm', 'LISA', 'barT']
L4 = list(map(normalize2, L1))
print(L4)
