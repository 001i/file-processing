import os

class wenjian:
    wenjianleixing=".txt"
    moren_wenjianshuliang=10
    path = 'D:/a_测试/'
    def addwja(path=path,shuliang=moren_wenjianshuliang):
        for i in range(shuliang):  # 这里创建10个文件夹
            # *定义一个变量判断文件是否存在,path指代路径,str(i)指代文件夹的名字*
            i+=1
            isExists = os.path.exists(path + str(i))
            if not isExists:  # 判断如果文件不存在,则创建
                os.makedirs(path + str(i))
                print("%s 目录创建成功" % i)
            else:
                print("%s 目录已经存在" % i)
                continue  # 如果文件不存在,则继续上述操作,直到循环结束


    def addwj(path=path,suliang=moren_wenjianshuliang,leix=wenjianleixing):
        for i in range(suliang):
            ##这里的./指代的是当前文件夹, %i表示文件的名称,a表示没有该文件就新建.
            lujing=path
            wenjianleix=leix
            f = open('%s%d'%(lujing,i+1) + wenjianleix,"a")
            # 写入文件，空
            f.write("")
            f.close()
        print("文件夹创建完毕")

# wenjian.addwja("D:/新建文件夹/",12)
# wenjian.addwj(path="D:/新建文件夹/",shuliang=12,leix=".txt")