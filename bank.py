import random
from mysqll import sql

# 老思路  通过链接数据库释放资源 追加在字典里面 比较耗时
zhang = list(sql().all())  #调用mysqll中的all方法 获取数据库中用户信息
# 基本信息
zhanghu= {}
for k in range(len(zhang)):
    zhanghu[zhang[k][0]]={
    'user':zhang[k][1],
    'password':zhang[k][2],
    'add':zhang[k][3],
    'money':zhang[k][4],
    'bank':zhang[k][5]}
print(zhanghu)

list=[]
# 开户
def kaihu():
    user=input("请输入您的名字：")
    password=input("请输入您的密码：")
    add=input("请输入您的地址：")
    zhanghao=random.randint(10000000,99999999)
    if zhanghao in zhanghu:
        print("存在相同的账号")
    else:
        if len(password)==6:
            list=[zhanghao,user,int(password),add,00,'中国农业银行的昌平沙河支行']
            p = sql()
            p.charu(list)
        else:
            print("您输入的密码长度不符合要求！！")

# kaihu()
# 存钱
def cunqian():
    zhanghao=input("请输入您的账号：")
    if zhanghao in zhanghu:
        money=int(input("请输入存入的金额："))
        zhanghu[zhanghao]['money']=money+int(zhanghu[zhanghao]['money'])
        zhi=[zhanghu[zhanghao]['money'],zhanghao]
        p = sql()
        p.update(zhi)
        print("存钱成功 嘿嘿")
        print('您账户的余额为：',zhanghu[zhanghao]['money'])
    else:
        print("账号不存在")

# cunqian()


# 取钱
def quqian():
    zhanghao=input("请输入您的账号：")
    if zhanghao in zhanghu:
        i=int(input("请输入取出的金额："))
        if i<int(zhanghu[zhanghao]['money']):
            zhanghu[zhanghao]['money']=int(zhanghu[zhanghao]['money'])-i
            zhi = [zhanghu[zhanghao]['money'], zhanghao]
            p = sql()
            p.update(zhi)
            print("取钱成功 嘿嘿")
            print("您账户的余额为：",zhanghu[zhanghao]['money'])
        else:
            print("您的账户余额不足")
    else:
        print("账号不存在")

# quqian()

# 转账
def zhuanzhang():
    hao=input("请输入您的账号：")
    if hao in zhanghu:
        zhanghao2 = input("请输入你要转入的账号：")
        if zhanghao2 in zhanghu:
            password = input("请输入您的密码：")
            if password == zhanghu[hao]['password']:
                i = int(input("请输入转出的金额："))
                if i<=int(zhanghu[hao]['money']):
                    zhanghu[hao]['money']=int(zhanghu[hao]['money'])-i
                    zhi = [zhanghu[hao]['money'], hao]
                    p = sql()
                    p.update(zhi)
                    print("扣款成功 嘿嘿")
                    print("您账户的余额为：", zhanghu[hao]['money'])
                    zhanghu[zhanghao2]['money']=int(zhanghu[zhanghao2]['money'])+i
                    zhi1 = [zhanghu[zhanghao2]['money'], zhanghao2]
                    p = sql()
                    p.update(zhi1)

                    print("转账成功..")
                else:
                    print("您的账户余额不足")
            else:
                print("您输入的密码不正确！！")
        else:
            print("对方账户不存在")
    else:
        print("您的账户不存在")
# zhuanzhang()


def cahxun():
    zhanghao = input("请输入您的账号：")
    if zhanghao in zhanghu:
        print("以下就是查询的信息")
        print(zhanghu[zhanghao])
    else:
        print("没有您查询的账户！！")


def zhu():
   while True:
        print("*************")
        print("1        开户")
        print("2        存钱")
        print("3        取钱")
        print("4        转账")
        print("5        查询")
        print("6        退出")
        print("*************")
        i = int(input("请输入您要查询的业务："))
        if i ==1:
            kaihu()
        elif i==2:
            cunqian()
        elif i==3:
            quqian()
        elif i==4:
            zhuanzhang()
        elif i==5:
            cahxun()
        elif i==6:
            break
        else:
            print("您输入的数据不符合要求11")

zhu()