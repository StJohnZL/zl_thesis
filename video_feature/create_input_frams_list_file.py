#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : a.py
# @Author: ZL
# @Date  : 2018/4/22
# @Desc  : 生成网络输入视频的帧列表文件，格式：<string_path> <start_frame> <label> ，
#          对于label来说：boat：0，car：1，tank：2，airplane：3

import os
import string

path_str= "/Users/uxin/Desktop/张磊本科毕业论文/thesis_data/split_frams"
frams_list_file_path = "/Users/uxin/Desktop/张磊本科毕业论文/thesis_data/my_input_frams_list_file.txt"

root_path = os.path.abspath(path_str)

# 获取指定目录下的所有文件夹
secode_dir_list = os.listdir(path_str)
print(secode_dir_list)

for seconde_dir in secode_dir_list:
    # 获取第二级文件夹的绝对路径
    secode_dir_abspath = os.path.join(path_str,seconde_dir)

    # 获取第二级文件夹下的文件夹列表
    first_dir_list = os.listdir(secode_dir_abspath)

    for first_dir in first_dir_list:
        source_path = os.path.join(seconde_dir,first_dir)
        source_abspath = os.path.join(path_str,source_path)

        # 帧文件列表
        files_list = os.listdir(source_abspath)
        # 一个视频帧的数量
        files_cnt = len(files_list)

        # 每16帧为一clip
        lines_str_list = []
        if files_cnt>=1:
            start_frams = 1
            for i in range(0,(files_cnt)/1+1):
                # boat：0，car：1，tank：2，airplane：3
                label=""
                if string.find(source_path,"boat") != -1:
                    label="0"
                elif string.find(source_path,"car") != -1:
                    label = "1"
                elif string.find(source_path,"tank") != -1:
                    label = "2"
                elif string.find(source_path,"airplane") != -1:
                    label = "3"
                # 格式：<string_path> <start_frame> <label>
                input_list_line_str = source_path + " " + str(start_frams) + " " + label + "\r\n"
                lines_str_list.append(input_list_line_str)
                #start_frams+=16
                start_frams+=1

        # 将一个视频的内容写入
        f = open(frams_list_file_path,"aw")
        f.writelines(lines_str_list)
        f.close()




















































