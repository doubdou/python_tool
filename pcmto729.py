#!/usr/bin/python  
# -*- coding:utf8 -*-  
import os
import re

main = "cp_g729_encoder.exe %s %s"

def get_dir(path):
    for dirname, _, files in os.walk(path):
        for file in files:
            abs_name = os.path.join(dirname, file)
            if abs_name.endswith("txt"):
            #if re.match('(.*).txt', abs_name):
                continue
            print(abs_name)
            if abs_name.endswith("pcm"):
                print(abs_name[:-3]+'G729')
                r_v = os.system(main % (abs_name, abs_name[:-3]+'G729'))
                os.remove(abs_name)


if __name__ == '__main__':
    #get_dir("E:\\test")
    get_dir("E:\\3")


