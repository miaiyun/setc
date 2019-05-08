TempStr = input("请输入有符号得温度值： ")
if TempStr[-1] in ['F', 'f']:
        C = (eval(TempStr[0:-1]) - 32)/1.8
        print("转换到摄氏度为c".format(C))
        print(C)
elif TempStr[-1] in ['C', 'c']:
        F = 1.8*eval(TempStr[0:-1])+32
        print("摄氏度转换到F".format(F))
else:
    print("输入错误：")