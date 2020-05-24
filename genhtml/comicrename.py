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

    path_top_str = r"J:\新建文拳超人"
    path_top = Path(path_top_str)
    for child_dir in path_top.iterdir():
        if child_dir.is_dir():
            dir_name = child_dir.name
            print("dir = %s" % dir_name)

            child_p = Path(child_dir)
            for file1 in child_p.iterdir():
                # print("file = %s" % file1.name)
                target = path_top_str + "\\" + dir_name + "_" + file1.name
                file1.rename(target)
        else:
            print("%s not dir" % str(child_dir))

    print("================================ finish")


if __name__ == "__main__":
    main()
