# coding: utf-8
"""read_picture.py
~~~~~~~~~~~~~
本模块主要负责读取图片中的文字

:copyright: (c) 2021 by Zhichao Xia
:modified: 2021-05-27
"""
import os
import pytesseract
from PIL import Image

path = "C:/Users/xzc/Desktop/图片"
for i in os.listdir(path):
    pathAll = path + '/' + i
    image = Image.open(pathAll)
    image = image.convert('L')
    content = pytesseract.image_to_string(image, lang='chi_sim')
    print("%s>>>" % i, content)