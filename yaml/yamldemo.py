# coding: utf-8

import unittest
import yaml


class YamlDemo(unittest.TestCase):

    @staticmethod
    def test1():
        data = yaml.load(open("abacus_learner.yaml"))
        print(data['slots'])
        print(data['online_runner']['working_root'])
        print(data['monitors'][0])
