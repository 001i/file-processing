from gunneng import addwenjian


print("欢迎使用")

# 4.批量
# 5.自定义

class wen:
    wenban = """
        1.批量创建文件夹
        2.批量创建文件
        3.批量重命名
        4.批量移动路径
        5.批量压缩
        6.设置
        7.帮助
        8.退出
        """
    def __init__(self):
        print(self.wenban)

wen()

while True:
    bianhao = input("请输入编号")
    suzi=int(bianhao)
    if suzi<=8:
        print(wen.wenban)
        if 1 == suzi:
            print("1")
            continue
        if 2 == suzi:
            addwenjian.wenjian.addwj()
            continue
        if 3 == suzi:
            print("1")
            continue
        if 4 == suzi:
            print("2")
            continue
        if 5 == suzi:
            print("2")
            continue
        if 6 == suzi:
            print("1")
            continue
        if 7 == suzi:
            print("2")
            continue
        if 8 == suzi:
            print("""感谢使用本程序
现在版本为1.0
比之前写的旧版本提升巨大
本次软件为python所写
作者是
        ——haha
        ——001i
""")
            break
    else:
        print(wen.wenban)
        print("输入不正确请从新输入")