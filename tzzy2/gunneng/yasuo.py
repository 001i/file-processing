import imghdr
import os
from PIL import Image
from gunneng.beifen import *
def compress_images(input_folder, output_folder, quality):
    # 检查输出文件夹是否存在，如果不存在则创建
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # 检查文件是否为图像文件
        if os.path.isfile(input_path) and imghdr.what(input_path):
            # 打开图像文件
            image = Image.open(input_path)

            # 压缩图像并保存到输出文件夹中
            image.save(output_path, optimize=True, quality=quality)

            # 关闭图像文件
            image.close()
    print("压缩完成")



def yashuo(lujing1,lujing2,bili=20):
    # 定义输入文件夹路径
    input_folder = lujing1+"/"  # 替换为实际的文件夹路径

    # 定义输出文件夹路径
    output_folder = lujing2+"/"  # 替换为实际的文件夹路径

    # 定义压缩比例（0-100）
    compression_quality = bili  # 替换为实际的压缩比例

    # 调用压缩函数
    compress_images(input_folder, output_folder, compression_quality)

# yashuo("C:/Users/kook/Desktop/安全员寸照","C:/Users/kook/Desktop/cc",20)

# shuru=beifen.diaoyong("浏览文件路径","4")
# shucu=beifen.diaoyong("输出文件路径","4")
# yasuobi = int(beifen.diaoyong("压缩比", "4")[0])
# print(shuru[0])
# print(shucu[0])
# print(yasuobi)
#
#
# yashuo(shuru[0]+"/",shucu[0]+"/",yasuobi)

# shuru[0]结果是C:/Users/kook/Desktop/安全员寸照
# shucu[0]结果是C:/Users/kook/Desktop/cc
# yasuobi[0]结果是45
# 为什么报错