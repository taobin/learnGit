weight =float(input('请输入一个数字'))
if weight<18.5:
    print('过轻')
elif weight>=18.5 and weight<=25:
    print('正常')
elif weight>25 and weight<28:
    print('过重')
elif weight>=28 and weight<32:
    print('肥胖')
elif weight>32:
    print('严重肥胖')
