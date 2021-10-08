from HTMLTestRunner import HTMLTestRunner
import unittest
from unittestreport import TestRunner

t1 = unittest.defaultTestLoader.discover(r"D:\PyCharm 2019.2.5\untitled\day01_1\银行系统",pattern="testmain.py")


# runner1= HTMLTestRunner.HTMLTestRunner(
#     title="HtmlTestRunner生成的报告",
#     description="银行添加账号/走账报告",
#     verbosity=1,
#     stream= open("HtmlTestRunner生成的报告.html",mode="w+",encoding="utf-8")
# )
#
# runner1.run(t1)

runner2= TestRunner(t1,
           title="TestRunner生成的报告",
           templates=3,
           report_dir="报告",
           desc="这是一份描述银行账户管理的报告",
           tester="芮振阳",
           filename="TestRunner生成的报告.html",

)
runner2.run()

runner2.send_email(
    host="smtp.qq.com",
    port=465,
    user="1484193144@qq.com",
    password="gqjpnynjuorhhaeg",
    to_addrs="1484193144@qq.com"

)
