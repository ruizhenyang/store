from  unittest import TestCase
from mysqll import sql
from ddt import data
from ddt import ddt
from ddt import unpack

list=[
[43536348,'芮阳4',121212,'上海',20,'中国农业银行的昌平沙河支行'],
[47263828,'芮阳4',121212,'上海',20,'中国农业银行的昌平沙河支行'],
[43995018,'芮阳4',121212,'上海',20,'中国农业银行的昌平沙河支行'],
[43086358,'芮阳4',121212,'上海',20,'中国农业银行的昌平沙河支行']
]

@ddt()
class Testmain(TestCase):
    @data(*list)
    @unpack
    def testkaihu(self,list):

        p =sql()
        guo = p.charu(list)
        self.assertEqual(guo,1)

    def testzhuanzhang(self):
        zhi=[888888,43215618]
        p = sql()
        guo = p.update(zhi)
        self.assertEqual(guo,2)


# from  unittest import TestCase
# from mysqll import sql
#
# class Testmain(TestCase):
#     def testkaihu(self):
#         list = [35582289, '芮阳8', 121212, '上海', 20, '中国农业银行的昌平沙河支行']
#         p =sql()
#         guo = p.charu(list)
#         self.assertEqual(guo,1)
#
#     def testzhuanzhang(self):
#         zhi=[9999000,43215618]
#         p = sql()
#         guo = p.update(zhi)
#         self.assertEqual(guo,2)