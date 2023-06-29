import datetime
import os
from beifen import *
from weizi import *

class xingxi:
    # 时间
    def teim(self=None):
        current_time = datetime.datetime.now()

        # 获取年、月、日、时、分、秒
        year = current_time.strftime("%Y")
        month = current_time.strftime("%m")
        day = current_time.strftime("%d")
        hour = current_time.strftime("%H")
        minute = current_time.strftime("%M")
        second = current_time.strftime("%S")

        # 构建日期和时间的描述
        date_description = f"{year}年{month}月{day}日"
        time_description = f"{hour}时{minute}分{second}秒"

        # 使用符号连接日期和时间描述
        datetime_description = f"{date_description}-{time_description}"

        print("当前日期和时间：", datetime_description)
        return datetime_description

    #前缀
    def qianzui(path,text,shuzu):
        # 当前路径名
        current_folder = os.path.basename(path)
        # 获取当前时间
        teim = xingxi.teim()
        for i in shuzu:
            beifen.beifenwenben(name=current_folder + "-" + teim, text="ren " + text + i + "\000%s" % (i) + "\n")
            os.rename('%s/%s' % (path, i), '%s/%s%s' % (path, text, i))
            print(i + "--->" + text + i)

    #后缀
    def houzui(path, text, shuzu):
        # 当前路径名
        current_folder = os.path.basename(path)
        # 获取当前时间
        teim = xingxi.teim()

        for i in shuzu:
            wenjianming = os.path.splitext(i)[0]
            houzui = os.path.splitext(i)[1]
            beifen.beifenwenben(name=current_folder + "-" + teim, text="ren " +wenjianming+text+houzui + "\000%s" % (i) + "\n")
            # input("名字"+wenjianming)
            # input("后缀"+houzui)
            os.rename('%s/%s' % (path, i), '%s/%s%s%s' % (path, wenjianming, text, houzui))
            print(i + "--->" + wenjianming + text + houzui)

    #时间
    def shijian(path, shuzu):
        # 当前路径名
        current_folder = os.path.basename(path)
        # 获取当前时间
        teim = xingxi.teim()

        qianname = weizi.qian(shuzu, teim)
        # for i in x, c:
        for i,j in zip(shuzu,qianname):
            #创建备份
            beifen.beifenwenben(name=current_folder + "-" + teim, text="ren " + j + "\000%s" % (i) + "\n")
            os.rename('%s/%s' % (path, i), '%s/%s' % (path, j))
            print(i + "--->" + j)