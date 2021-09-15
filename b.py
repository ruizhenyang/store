import random
an=random.randint(0,20)
i = 0
ran = 500
while i <= 7:
    num=int(input("请输入一个数字: "))
    if num > an:
        ran = ran - 100
        print("数字猜大了呦")
    elif num < an:
        ran = ran - 100
        print("数字猜小了呦")
    elif num == an:
        ran = ran + 10
        print("猜对啦！小可爱真棒！",num,ran,"要继续猜下去吗？")
        s = input("请输入Yes或No")
        print(type(s),s)
        if s == "Yes":
            continue
        elif s == "No":
            break
        else:
            break
    if ran <= 0:
        break
    i = i + 1