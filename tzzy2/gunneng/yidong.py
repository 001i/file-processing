import shutil
import os

class wjcz:
    #所有
    def wenjian(yi,er,lx):
        source = yi
        destination = er
        if "移动" == lx:
            # 移动
            shutil.move(source, destination)
        if "复制" == lx:
            # 获取源文件夹的名称
            folder_name = os.path.basename(source)
            # 拼接目标文件夹路径
            target_folder = os.path.join(destination, folder_name)
            # 复制源文件夹中的内容到目标文件夹中
            shutil.copytree(source, target_folder)
            # shutil.copytree(source, destination, dirs_exist_ok=True)
        else:
            print("类型错误")
