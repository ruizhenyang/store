import pymysql

class sql:
    # *******************************查询信息**********************************************
    def all(self):     #目的查询普通用户表中所有数据
        d1 = pymysql.connect(host="localhost",user="root",password="root",database="test")
        cursor = d1.cursor()
        sql = "select * from adduser"
        cursor.execute(sql)
        userall = cursor.fetchall()
        # print(userall)
        d1.commit() #刷新
        cursor.close()
        d1.close()
        return userall

    # **********************************创建新用户**********************************************
    def charu(self,list):
        d2 = pymysql.connect(host="localhost", user="root", password="root", database='test')
        cursor = d2.cursor()
        sql2 = "INSERT INTO adduser VALUES (%s,%s,%s,%s,%s,%s)"  # (43215678,'芮阳',121212,'上海',20,'中国农业银行的昌平沙河支行')
        cursor.execute(sql2,list)
        print("恭喜你，账户创建成功")
        d2.commit()
        cursor.close()
        d2.close()
        return 1    #单元测试用于检测有无返回值来判定结果



    # **********************************存钱取钱转账*******************************************
    def update(self,zhi):
        d3 = pymysql.connect(host="localhost",user="root",password="root",database="test")
        cursor = d3.cursor()
        sql="UPDATE adduser SET 余额 =%s WHERE 账号=%s"
        cursor.execute(sql,zhi)
        d3.commit()
        cursor.close()
        d3.close()
        return 2
