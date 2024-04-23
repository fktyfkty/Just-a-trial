# Python的模块
# 模块是一个Python文件，里面有类，函数，变量等，可以直接拿来用

""" 模块和包在开头就要导入"""
# 导入模块就是导入一个代码文件
# 基本语法： import 模块名
#          模块名.功能名（）
import time # time是Python内置的模块,里面所有函数都能用
print("a")
time.sleep(5)
print(1)

# 用from完成模块的导入：只用模块中的某个方法（功能）
from time import sleep
print("a")
sleep(5)
print(1)

# from time import *  ：调用模块全部功能，且调用不用加点

# as:给模块或者模块中的功能取一个别名
import time as t
t.sleep(5)

from time import sleep as sl
# 模块导入语句变灰表示未被使用


# 自定义模块：自己写一个.py文件，作为模块，
# 按正常模块导入格式导入另一个文件即可
import my_module1
my_module1.test(1,2)

# 导入不同模块的同名功能，后面的功能覆盖前面的
#  在模块内部测试调用功能函数，在导入时也会被调用
# 在模块内用文件内置变量__name__来防止导入时功能函数被调用
# import *时，只导入模块__all__列表中的功能函数


# python 包的自定义：
"""
就是建一个文件夹，在文件夹包含写自己的模块（代码文件），
模块里写自己想要的功能（函数），再导入主文件即可。
包更方便管理模块

"""
# Python包是什么
# 包是一个文件夹，装的是模块和__init__.py
#  __init__.py是包的特征

# 导入包
import my_package.my_moddule_2
import my_package.module3
my_package.my_moddule_2.infomat()
my_package.module3.info2()

from my_package import my_moddule_2
my_moddule_2.infomat()

# 导入包时用__all__控制import*导入的范围
# 此处__all__写在init里面



# 安装第三方包：pip,用pip安装的包是在原本python最基本解释器里面的
# 默认安装的网站是在国外会比较慢，可以用VPN或国内网站来下（好像不支持）
# 也可以用pycharm安装:也要用VPN






