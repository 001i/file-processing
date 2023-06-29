import os
from beifen import *
from gunneng import get_xingxi


# 已写完
# 给文件是用来引用目录下的文件，及文件夹的


class mulu:
    #仅保留文件，排除文件夹
    def wj_shuliang(path):
        files_and_folders = os.listdir(path)
        # 仅保留文件，排除文件夹
        files = [f for f in files_and_folders if os.path.isfile(os.path.join(path, f))]
        # 创建空数组
        file_names = []
        # 当前路径名
        # current_folder = os.path.basename(lur)
        #获取当前时间
        teim=get_xingxi.xingxi.teim()
        # 打印所有文件名
        for file in files:
            # beifen.beifen.beifenwenben(name=current_folder+"-"+teim,text=file+"\n")
            file_names.append(file)
            wenjianming = os.path.splitext(file)[0]
            beifen.beifenwenben(name="记录文件无后缀——%s"%(teim),text=wenjianming+"\n")
            beifen.beifenwenben(name="记录文件——%s" % (teim), text=file + "\n")
        # 打印文件名数组
        print(file_names)
        # print("一创建备份成功:C:/KCL/" + current_folder+"-"+teim)
        return file_names


    #文件夹
    def wja_shuliang(path):
        files_and_folders = os.listdir(path)
        # 仅保留文件夹，排除文件
        folders = [f for f in files_and_folders if os.path.isdir(os.path.join(path, f))]
        # 创建空数组
        file_names = []
        # 当前路径名
        # current_folder = os.path.basename(lur)
        # 获取当前时间
        teim = get_xingxi.xingxi.teim()
        # 打印所有文件夹的名称
        for file in folders:
            # beifen.beifen.beifenwenben(name=current_folder + "-" + teim, text=folder + "\n")
            file_names.append(file)
            wenjianming = os.path.splitext(file)[0]
            beifen.beifenwenben(name="记录文件夹无后缀——%s" % (teim), text=wenjianming + "\n")
            beifen.beifenwenben(name="记录文件夹——%s" % (teim), text=file + "\n")
        # print(file_names)
        # print("备份成功:C:/KCL/" + current_folder + "-" + teim)
        return file_names

    #文件+文件夹
    def wjawj_shuliang(path):
        files_and_folders = os.listdir(path)

        # 仅保留文件夹和文件，排除其他类型的项
        folders = [f for f in files_and_folders if os.path.isdir(os.path.join(path, f))]
        files = [f for f in files_and_folders if os.path.isfile(os.path.join(path, f))]
        # 获取当前时间
        teim = get_xingxi.xingxi.teim()
        yi=[]
        # 打印所有文件夹的名称
        # print("文件夹名:")
        for folder in folders:
            wenjianming = os.path.splitext(folder)[0]
            beifen.beifenwenben(name="记录文件+文件夹无后缀——%s" % (teim), text=wenjianming + "\n")
            beifen.beifenwenben(name="记录文件+文件夹——%s" % (teim), text=folder + "\n")
            yi.append(folder)
            # print(folder)


        # 打印所有文件的名称
        # print("文件名:")
        for file in files:
            wenjianming = os.path.splitext(file)[0]
            beifen.beifenwenben(name="记录文件2+文件夹2无后缀——%s" % (teim), text=wenjianming + "\n")
            beifen.beifenwenben(name="记录文件2+文件夹2——%s" % (teim), text=file + "\n")
            yi.append(file)
            # print(file)

        # for i in yi:
        #     print(i)
        return yi

    # 目录下的所有文件
    def sywj_shuliang(path):
        suzu=[]
        # 所有文件
        teim = get_xingxi.xingxi.teim()
        for filepath, dirnames, filenames in os.walk(r'%s' % (path)):
            for filename in filenames:
                wenjianming = os.path.splitext(filename)[0]
                beifen.beifenwenben(name="记录所有文件无后缀——%s" % (teim), text=wenjianming + "\n")
                beifen.beifenwenben(name="记录所有文件——%s" % (teim), text=filename + "\n")
                # print(filename+"--->"+text+"测试")
                suzu.append(filename)
        return suzu

# mulu.wj_shuliang("")