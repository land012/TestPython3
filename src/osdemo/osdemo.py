import os

__author__ = 'xudazhou'


if __name__ == "__main__":
    # print(os.getcwd())  # D:\_python\TestProj\src\com\demo\helloworld

    print(os.name)  # nt

    print(os.path.exists("E:\\TDDOWNLOAD\\工作簿1.xlsx"))

    # 环境变量
    print(os.getenv("JAVA_HOME"))  # D:\ProgramDev\Java\jdk1.8.0_65
