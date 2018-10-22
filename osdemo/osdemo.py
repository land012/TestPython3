import os

__author__ = 'xudazhou'


def main():
    # print(os.getcwd())  # D:\_python\TestProj\src\com\demo\helloworld

    print(os.name)  # nt

    print(os.sep)

    print(os.path.exists("E:\\TDDOWNLOAD\\工作簿1.xlsx")) # False

    # 环境变量
    print(os.getenv("JAVA_HOME"))  # D:\ProgramDev\Java\jdk1.8.0_65

    """
    如果不在 pyCharm 中执行，返回 None

    原始格式：分号分隔，不换行
    D:\_python\TestPython3\clazz
    D:\_python\TestPython3\file
    D:\_python\TestPython3\src
    D:\_python\TestPython3\helloworld
    D:\_python\TestPython3\memory_profiler_d
    D:\_python\TestPython3\src\hello
    D:\_python\TestPython3\src\subprocess
    D:\_python\TestPython3\src\sysdemo
    D:\_python\TestPython3\src\osdemo
    D:\_python\TestPython3\src\zipdemo
    D:\_python\TestPython3\webtest
    D:\_python\TestPython3\threaddemo
    D:\_python\TestPython3\flaskdemo
    D:\_python\TestPython3\struct
    D:\_python\TestPython3
    D:\_python\TestPython3\src\stringdemo
    """
    print(os.environ.get("PYTHONPATH"))

if __name__ == "__main__":
    main()
