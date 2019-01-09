# coding: utf-8

"""
comic html
"""
from pathlib import Path

def main():

    origin_f = open("index.html")
    origin_html = origin_f.read()

    path_top = "F:\Game\_1_korea\[疾風]"

    p1 = Path(path_top)

    for path_child in p1.iterdir():
        if path_child.is_dir():
            html_file = open("%s.html" % path_child, mode="w", encoding="utf-8")
            html_file.write(origin_html)

            p2 = Path(path_child)
            for picname in p2.iterdir():
                # print(picname.name)
                html_file.write("<img src=\"%s/%s\" /><hr/>\n" % (path_child.name, picname.name))
            html_file.write("</body></html>")
            html_file.close()
        else:
            print("%s skip" % path_child)

    print("===== finish =====")


if __name__ == "__main__":
    main()
