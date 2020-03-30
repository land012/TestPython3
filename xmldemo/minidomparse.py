# coding: utf-8

import xml.dom.minidom

__author__ = 'xudazhou'


if __name__ == "__main__":
    xmlf = open("job.xml", encoding="utf-8")
    dom = xml.dom.minidom.parseString(xmlf.read())

    # dom = xml.dom.minidom.parse("job.xml")

    root = dom.documentElement
    print(root.nodeName)  # configuration
    print(root.nodeValue)  # None
    print(root.nodeType)  # 1
    print(xml.dom.minidom.Node.ELEMENT_NODE)  # 1
    print(xml.dom.minidom.Node.ATTRIBUTE_NODE)  # 2
    print(xml.dom.minidom.Node.TEXT_NODE)  # 3
    properties = root.getElementsByTagName("property")

    dict1 = dict()
    for p in properties:
        # print(p.nodeName)  # property
        # print(p.nodeType)  # 1
        name = p.getElementsByTagName("name")[0]  # <name> 标签
        # print(name.nodeType)  # 1
        # print(name.nodeValue)  # None

        cfg_name = name.firstChild
        # print(cfg_name.nodeType)  # 3

        # 这两个值相同
        # print(cfg_name.data)
        # print(cfg_name.nodeValue)

        # if cfg_name.data == "mapred.job.name":
        #     print(p.getElementsByTagName("value")[0].firstChild.data)

        dict1[cfg_name.data] = p.getElementsByTagName("value")[0].firstChild.data

    print(dict1)
