import os

#该文件一写完，是创建备份目录的

class beifen:
    KCL = "KCL"
    lur="C:/KCL"
    cj="创建文件记录"
    mm="重命名文件记录"
    yd="移动文件记录"
    ys="压缩文件记录"
    zdy="自定义文件记录"
    cz="操作记录"
    qt="其他记录"

    # 创建备份文件夹
    def __init__(self):
        path = 'C:/KCL'
        paths=[]
        directories = ['创建文件记录', '重命名文件记录', '移动文件记录', '压缩文件记录', '自定义文件记录', '操作记录',
                       '其他记录']
        for i in directories:
            paths = os.path.join(path, i)

        if not os.path.exists(paths):
            os.makedirs(paths)
            print(f"成功创建文件夹：{paths}")
        else:
            print("yes")
            # print(f"文件夹已存在：{paths}")

    # 示例用法


    def xuanze(sz):
        if "0"==sz:
            return beifen.lur
        if "1"==sz:
            zi = beifen.lur + "/" + beifen.cj
            return zi
        if "2"==sz:
            zi = beifen.lur + "/" + beifen.mm
            return zi
        if "3"==sz:
            zi = beifen.lur + "/" + beifen.yd
            return zi
        if "4"==sz:
            zi = beifen.lur + "/" + beifen.ys
            print(zi)
            return zi
        if "5"==sz:
            zi = beifen.lur + "/" + beifen.zdy
            return zi
        if "6"==sz:
            zi = beifen.lur + "/" + beifen.cz
            return zi
        else:
            return beifen.lur

    # 创建备份文档
    def beifenwenben(name,text,houzhui=".txt"):
        f = open('%s%s'%('C:/KCL/',name) + houzhui,"a")
        # 写入文件，空
        f.write(text)
        f.close()

    def beifenwenben2(path,name,text,houzhui=".txt"):
        f = open(path+"/"+name + houzhui,"a")
        # 写入文件，空
        f.write(text)
        f.close()

    #创建覆盖文件
    def create_text_file(name,text="",shuzi="0",houzhui=".txt"):
        zi=beifen.xuanze(shuzi)
        hh = zi +"/"+ name+houzhui
        beifen.beifenwenben2(zi,name,text)
        with open(hh, 'w') as file:
            file.write(text)



    #调用文本
    def diaoyong(name,shuzi="0",houzhui=".txt"):
        zi = beifen.xuanze(shuzi)
        lines = []
        with open(zi+"/"+name+houzhui, 'r') as file:
            for line in file:
                lines.append(line.strip())
        return lines



# xx=beifen.diaoyong("输出文件路径","4")
# print(xx[0]+"ee")
# beifen.create_text_file("创建类型记录","nihao","1")
# cc=beifen.diaoyong("创建类型记录", "1")
# print(cc[0])