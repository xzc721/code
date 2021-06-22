# coding: utf-8
"""quchong.py
~~~~~~~~~~~~~
本模块主要负责对文件去重
将B文件出现，A文件中未出现的行写入新文件C中

:copyright: (c) 2021 by Zhichao Xia
:modified: 2021-05-06
"""
# 创建新文件C
write_path = open("../../../title_processed/data/new_company.txt", 'w', encoding='utf-8')
# 读取A文件，并利用set方式自去重
test_set = set()
with open("../../../title_processed/data/other.txt", 'r', encoding='utf-8') as f:
    for each_line in f.readlines():
        test_set.add(each_line)
# 读取B文件，并将A中没有的行写入新文件C中
with open("../../../title_processed/data/20000company.txt", 'r', encoding='utf-8') as f1:
    for each_data in f1.readlines():
        if each_data not in test_set:
            write_path.write(each_data)









