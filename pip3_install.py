# -*- coding: utf-8 -*-
import os

#在Libs中输入需要的扩展库
Libs=[
    "pyinstaller",
    "jieba",
    "requests",
    "win10toast",
    #"win11toast",
    "numpy",
    "matplotlib",
    "pandas",
    "scipy",
    "openpyxl",
    #"PyQtChart",
    #"PyQt6-Charts",
    "PySide6"
]

#官方下载地址及国内部分镜像源网址
Web={
    "pypi":"https://pypi.org/simple",
    "aliyun":"https://mirrors.aliyun.com/pypi/simple/",
    "tencent":"https://mirrors.cloud.tencent.com/pypi/simple",
    "douban":"https://pypi.douban.com/simple/",
    "tsinghua":"https://pypi.tuna.tsinghua.edu.cn/simple",
    "ustc":"https://pypi.mirrors.ustc.edu.cn/simple"
}

#选择镜像源
web=" -i "+Web["aliyun"]

#更新pip
try:
    print("开始更新pip")
    print("---------------------------------")
    os.system("pip3 install -U pip"+web)
    print("---------------------------------")
    print("pip更新成功")
except:
    print("---------------------------------")
    print("pip更新失败")

#更新setuptools
try:
    print("\n")
    print("开始更新setuptools")
    print("---------------------------------")
    os.system("pip3 install -U setuptools"+web)
    print("---------------------------------")
    print("setuptools更新成功")
except:
    print("---------------------------------")
    print("setuptools更新失败")

print("\n")
print("开始安装扩展库")
print("\n")

#安装扩展库
for Lib in Libs:
    try:
        print("开始安装"+Lib)
        print("---------------------------------")
        os.system("pip3 install "+Lib+web)
        print("---------------------------------")
        print(Lib+"安装成功")
        print("\n")
    except:
        print(Lib+"安装失败")

print("\n")
print("扩展库安装结束，请查看是否全部安装成功")
print("\n")

os.system("pip3 list")

os.system("pause")    