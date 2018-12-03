print('------------我爱鱼工作室----------')
#接收的是一个字符串
temp = input("猜猜现在我想的数字")
#转换字符串
guess=int(temp)
if guess==8:
    print("猜对了")
    print("也没有奖励")
else:
    print("猜错了，正确的是8")
print("游戏结束，不玩了")
