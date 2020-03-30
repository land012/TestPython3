# coding: utf-8

import xml.sax

__author__ = 'xudazhou'

class JobHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.curtag = ""
        self.key = ""
        self.res = dict()

    def startElement(self, tag, attributes):
        self.curtag = tag

    def endElement(self, tag):
        self.curtag = ""
        if tag == "value":
            self.key = ""

    def characters(self, content):
        if self.curtag == "name":
            self.key = content
        if self.curtag == "value":
            self.res[self.key] = content


    def get_config(self):
        return self.res


if __name__ == "__main__":
    parser = xml.sax.make_parser()
    handler = JobHandler()
    parser.setContentHandler(handler)
    parser.parse("job.xml")
    res1 = handler.get_config()
    print(res1["abaci.metamaster.name"])  # yq01-tianqi
