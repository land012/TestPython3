# coding: utf-8
"""
# Created by xudazhou at 2019/6/4
"""
import os


if __name__ == "__main__":
    pwd_list = ["123456",
        "1042313275",
        "G856924h",
        "R732581d",
        "Q374950g",
        "4X30652a",
        "52D73g61",
        "24G9381b",
        "9C2375k8",
        "31B56s89",
        "16H957f4",
        "357F64x8",
        "8Ua47532",
        "18Z653j7",
        "6Y5a8294",
        "74E285v3",
        "53T62J91",
        "81E74y92",
        "1T495g37",
        "39S16j85",
        "538Fv279",
        "47H95n31",
        "86H31g45",
        "1Z49v237",
        "92W5k831",
        "52T94s37",
        "39U61j85",
        "1W739h62",
        "5Y84q731",
        "20F47h93",
        "39Z7h425",
        "8T3691g5",
        "6R1p4295",
        "g/u2(b1I0=Dc&3t6",
        "gZu2(b1I0-Dc&3t6"]

    for pwd in pwd_list:
        ec = os.system("7z e 9999.rar -p" + pwd)
        print("ec = %d" % ec)
        if ec == 0:
            print(pwd)
            break
