import os

from gunneng.muluwenjian import mulu
from gunneng.get_xingxi import xingxi
from gunneng.beifen import beifen

class wenjianname:

    # 前缀
    def qian_zhui(path,text):
        xuanzei=input("""
        选择添加前缀类型
        1.文件 2.文件夹 3.文件+文件夹 4.目录下的所有文件\n""")
        if True:
            if "1"==xuanzei:
                shuzu=mulu.wj_shuliang(path)
                xingxi.qianzui(path,text,shuzu)

            if "2"==xuanzei:
                shuzu=mulu.wja_shuliang(path)
                xingxi.qianzui(path, text, shuzu)

            if "3"==xuanzei:
                shuzu = mulu.wjawj_shuliang(path)
                xingxi.qianzui(path, text, shuzu)

            if "4"==xuanzei:
                shuzu=mulu.sywj_shuliang(path)
                xingxi.qianzui(path,text,shuzu)




    # 后缀
    def hou_zhui(path,text):
        xuanzei = input("""
        选择添加后缀类型
        1.文件 2.文件夹 3.文件+文件夹 4.目录下的所有文件\n""")
        if True:
            if "1" == xuanzei:
                shuzu = mulu.wj_shuliang(path)
                xingxi.houzui(path, text, shuzu)

            if "2" == xuanzei:
                shuzu = mulu.wja_shuliang(path)
                xingxi.houzui(path, text, shuzu)

            if "3" == xuanzei:
                shuzu = mulu.wjawj_shuliang(path)
                xingxi.houzui(path, text, shuzu)

            if "4" == xuanzei:
                shuzu = mulu.sywj_shuliang(path)
                xingxi.houzui(path, text, shuzu)


    # 时间
    def shijian(path):
        xuanzei = input("""
        选择添加时间类型
        1.文件 2.文件夹 3.文件+文件夹 4.目录下的所有文件\n""")
        if True:
            if "1" == xuanzei:
                shuzu = mulu.wj_shuliang(path)
                xingxi.shijian(path, shuzu)

            if "2" == xuanzei:
                shuzu = mulu.wja_shuliang(path)
                xingxi.shijian(path, shuzu)

            if "3" == xuanzei:
                shuzu = mulu.wjawj_shuliang(path)
                xingxi.shijian(path, shuzu)

            if "4" == xuanzei:
                shuzu = mulu.sywj_shuliang(path)
                xingxi.shijian(path, shuzu)

wenjianname.hou_zhui("D:/a_测试/","ss")

    # 日期
    # def riqi(path,text):




    # 字符插入
    # def caru(self):
    #
    #     print()

    # # 数字
    # def shuzi(self):
    #     print()
    #
    # # a-z
    # def zimu(self):
    #     print()
    #
    # # excel
    # def excel(self):
    #     print()
    #
    # # 自定义
    # def zidingyi(self):
    #     print()

