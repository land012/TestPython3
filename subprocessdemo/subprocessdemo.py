# coding: utf-8

import subprocess
import unittest
import sys
import logging


class SubprocessDemo(unittest.TestCase):

    @staticmethod
    def test_1():
        """
        子进程的标准输出直接打印到屏幕，cp.stdout拿到的是None
        """
        cp = subprocess.run("echo %cd%", stdout=sys.stdout, stderr=sys.stderr, shell=True)
        print(cp.returncode)
        print("stdout=%s" % cp.stdout)
        print("stderr=%s" % cp.stderr)

    @staticmethod
    def test_cmd1():
        """
        测试 windows 命令
        中文乱码 todo
        方式1：
        工程 encoding 改为 gbk 可以解决乱码问题
        """
        cp = subprocess.run("dir .", stdout=sys.stdout, stderr=sys.stderr, shell=True)
        print(cp.returncode)
        print("stdout=%s" % cp.stdout)
        print("stderr=%s" % cp.stderr)

    @staticmethod
    def test_cmd2():
        """
        不会出现中文乱码
        universal_newlines 和 subprocess.PIPE 同时使用
        universal_newlines 表示以字符串输出，否则以字符输出
        """
        cp = subprocess.run("dir D:\\",
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            shell=True,
                            universal_newlines=True)
        print("exitcode=%d" % cp.returncode)
        print("stdout=%s" % cp.stdout)
        print("stderr=%s" % cp.stderr)

    @staticmethod
    def test_2_0():
        """
        universal_newlines
        stdout/stderr 以字符串输出
        """
        cp = subprocess.run("echo %cd%", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, universal_newlines=True)
        print(cp.returncode)
        print("stdout=%s" % cp.stdout)
        print("stderr=%s" % cp.stderr)

    @staticmethod
    def test_2():
        """
        stdout/stderr 以 bytes 输出
        字节 转 字符串
        去掉末尾的回车符和换行符
        或者 替换掉换行符
        如果不处理换行符，在 windows 下的换行符是 \r\n，在控制台输出时，会有问题，\r 会覆盖当前行的文本
        :return:
        """
        cp = subprocess.run("echo %cd%", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        print(cp.returncode)
        stdout_bytes = cp.stdout
        print(type(stdout_bytes))  # <class 'bytes'>
        print(stdout_bytes)  # b'D:\\_python\\TestPython3\\src\\subprocess\r\n'

        stdout_str1 = stdout_bytes.decode(encoding="utf-8")
        # stdout_str = stdout_bytes[:-2].decode(encoding='utf-8')
        # stdout_str = str(stdout_bytes[:-2], encoding="utf-8")
        stdout_str = stdout_bytes.replace(b"\r\n", b"\n").decode(encoding='utf-8')
        print("len(stdout_str)=%d" % len(stdout_str))  # len(stdout_str)=37
        print("stdout=%s" % stdout_str)  # D:\_python\TestPython3\src\subprocess
        print("stderr=%s" % cp.stderr)

    @staticmethod
    def test_3():
        """
        :return:
        """
        log1 = logging.getLogger("serverlog")
        log1.setLevel(logging.INFO)

        fh = logging.FileHandler("./server.log")
        formater = logging.Formatter(fmt='%(asctime)s %(levelname)s (%(lineno)d) - %(message)s',
                                     datefmt='%Y-%m-%d %H:%M:%S')
        fh.setFormatter(formater)

        log1.addHandler(fh)

        # AttributeError: 'Logger' object has no attribute 'fileno'
        cp = subprocess.run("echo %cd%", stdout=log1, stderr=subprocess.PIPE, shell=True)
        log1.info(cp.returncode)

        stdout_bytes = cp.stdout
        print(type(stdout_bytes))  # <class 'bytes'>
        print(stdout_bytes)  # b'D:\\_python\\TestPython3\\src\\subprocess\r\n'

        stdout_str = stdout_bytes.replace(b"\r\n", b"\n").decode(encoding='utf-8')
        print("len(stdout_str)=%d" % len(stdout_str))  # len(stdout_str)=37
        print("stdout=%s" % stdout_str)  # D:\_python\TestPython3\src\subprocess
        print("stderr=%s" % cp.stderr)
