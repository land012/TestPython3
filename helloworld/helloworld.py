# coding: utf-8

import os


def hello(username):
    print("Hello %s" % username)


def main():
    print(os.getcwd())  # D:\_python\TestPython3\helloworld
    print(__file__)  # D:/_python/TestPython3/helloworld/helloworld.py


if __name__ == "__main__":
    main()
