__author__ = 'xudazhou'

import pathlib
import os
import mimetypes

'''
处理指定路径下的所有文本文件
'''

p = pathlib.Path("F:\\ccc\\txt")

# mimetypes.add_type("text/plain", "txt")

for file in p.iterdir():
    # print(file)  # F:\ccc\txt\1.jpg
    fname = file.name
    # print(fname)  # 1.jpg

    if file.is_file():
        ext = os.path.splitext(fname)
        # print(ext)  # ('1', '.jpg')
        # print(mimetypes.types_map[ext[1]])  # text/plain
        if ext[1] == ".txt":
            print(file)
