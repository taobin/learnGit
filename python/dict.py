d = {'Michel': 95, 'Bob': 60, 'Tracy': 85}
c = d['Bob']
print(c)
for i in d:
    print(d[i])
m = d.get('cc', -1)
print(m)
h = 'cc' in d
print(h)

# 删除
d.pop('Bob')
d['cc'] = 60
for i in d:
    print(i)
