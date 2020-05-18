# download_pip(镜像加速）
window下更换镜像比较麻烦；由于系统重装导致在pycharm中下载的包和pip下载包的地址不一致，希望下载到pip下载的地址中去
效果：镜像加速
使用方法：
from download_quick.download_quick import DownLoad_Module as d
def download_module():
    '''下载bokeh'''
    module = 'bokeh'
    tm = d(module).download_module()
download_module()


下载效果：
Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple
Collecting module
