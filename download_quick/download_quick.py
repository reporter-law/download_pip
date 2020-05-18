# -*-  coding: utf-8 -*-
# Author: caowang
# Datetime : 2020
# software: PyCharm
# 收获：类名为空意味着着创建新类，类名不为空意味着继承他类；传参可以直接传，因为传给了__init__，而__init__即为类本身
import os

class DownLoad_Module():
    def __init__(self,module):
        self.module = module

    def download_module(self):
        os.system('pip install -i https://pypi.tuna.tsinghua.edu.cn/simple ' + self.module)

    def update_module(self):
        os.system('pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade ' + self.module)

    def update_pip(self):
        os.system('Python  -m pip install --upgrade ' + self.module)

    def delete_module(self):
        os.system('pip uninstall ' + self.module)
