#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pipenv install twine --dev

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'FastAudioVisal'
DESCRIPTION = 'A command tool  to deal with  the recognition in audiovisual domain. It is pipline tool for all of the work.'
URL = 'https://github.com/liupeng678/FastAudioVisual'
EMAIL = 'liupeng19970119@gmail.com'
AUTHOR = 'liupeng'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '0.1.0'

# What packages are required for this module to be executed?
REQUIRED = [
    'tensorflow', 'librosa', 'matplotlib', 'torch', # 'requests', 'maya', 'records',
]




import os
import io
import setuptools
 
here = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()
 
# 允许setup.py在任何路径下执行
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
 
setuptools.setup(
    name="FastAudioVisual", # 库名，需要在pypi中唯一
    version="0.0.1",                       # 版本号
    author="Peng Liu",               # 作者
    author_email="liupeng19970119@gmail.com",     # 作者邮箱（方便使用者发现问题后联系我们）
    description="A command tool  to deal with  the recognition in audiovisual domain. It is pipline tool for all of the work.", # 简介
    long_description=long_description,              # 详细描述（一般会写在README.md中）
    long_description_content_type="text/markdown",  # README.md中描述的语法（一般为markdown）
    url="https://github.com/liupeng678/FastAudioVisual",   # 库/项目主页，一般我们把项目托管在GitHub，放该项目的GitHub地址即可
    packages=setuptools.find_packages(),    #默认值即可，这个是方便以后我们给库拓展新功能的
    classifiers=[                    # 指定该库依赖的Python版本、license、操作系统之类的
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    install_requires=[               # 该库需要的依赖库
        # exapmle
        'tensorflow',
        'librosa',
        'matplotlib',       
        'torch',  
        'Django >= 1.11, != 1.11.1, <= 2',
    ],
    python_requires='>=3.6',
)