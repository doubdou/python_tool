#!/usr/bin/python  
# -*- coding:utf8 -*-  
import os
import re

fileList = []

def get_dir(path):
    for dirname, _, files in os.walk(path):
        for file in files:
            abs_name = os.path.join(dirname, file)
            if re.match('(.*).txt', abs_name):
                continue
            print(abs_name)


if __name__ == '__main__':
    get_dir("E:\\network_channel")

