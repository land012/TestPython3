# coding: utf-8
"""
# Created by xudazhou at 2019/3/8
从子目录 mv 到上级目录，并且文件名加上目录名
"""
from pathlib import Path


def main():
    # print(type(p1.parent))  # <class 'pathlib.WindowsPath'>
    # p2 = Path(str(p1.parent) + "\\2.txt")
    # p1.rename(p2)

    path_top_str = r"F:\Game\新建文件夹\_1_3d\[3D]Under Corve01-04+紅警"
    path_top = Path(path_top_str)
    for child_dir in path_top.iterdir():
        if child_dir.is_dir():
            dir_name = child_dir.name
            for file in child_dir.iterdir():
                target = path_top_str + "\\" + dir_name + "_" + file.name
                file.rename(target)
        else:
            print("%s not dir" % str(child_dir))

    print("================================ finish")


if __name__ == "__main__":
    main()
