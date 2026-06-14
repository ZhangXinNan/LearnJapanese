
import os
import argparse
import numpy as np
# import cv2
from PIL import Image


from PIL import Image

def png_to_jpg(png_path, jpg_path):
    # 1. 打开 PNG 图片
    with Image.open(png_path) as img:
        # 检查图片是否包含透明通道 (RGBA 或 P 模式)
        if img.mode in ('RGBA', 'P'):
            # 创建一个相同大小的白色背景画布
            # (255, 255, 255) 代表白色，如果你想要黑色可以换成 (0, 0, 0)
            background = Image.new("RGB", img.size, (255, 255, 255))
            
            # 将原图粘贴到白色背景上，并使用原图的 alpha 通道作为遮罩（mask）
            # 这样透明的地方就会变成白色
            background.paste(img, (0, 0), img.convert("RGBA"))
            
            # 2. 保存为 JPG，可以设置 quality（质量）参数（1-100）
            background.save(jpg_path, "JPEG", quality=90)
        else:
            # 如果本来就是 RGB 模式（没有透明度），直接转换保存即可
            img.convert("RGB").save(jpg_path, "JPEG", quality=90)

    # print(f"转换成功: {jpg_path}")

# 调用示例
# png_to_jpg("input.png", "output.jpg")

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('in_dir')
    # parser.add_argument('out_dir', default=None)
    return parser.parse_args()


def main(args):
    # out_dir = args.in_dir if args.out_dir is None else args.out_dir
    for filename in os.listdir(args.in_dir):
        name, suffix = os.path.splitext(filename)
        if suffix.lower() not in ['.png', '.jpeg', '.bmp']:
            continue
        input = os.path.join(args.in_dir, filename)
        output = os.path.join(args.in_dir, name + '.jpg')
        png_to_jpg(input, output)
        print(input, os.path.getsize(input) // 1024, 'KB')
        print(output, os.path.getsize(output) // 1024, 'KB')
        


if __name__ == '__main__':
    main(get_args())


