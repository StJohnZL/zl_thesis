#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : specify_video_class.py
# @Author: ZL
# @Date  : 2018/5/5
# @Desc  : 为每一个视频指定分类
import os


def specify_video_class(path, class_dict):
    # 根目录
    one_path_dirs = os.listdir(path)
    # 定义视频类别字典
    video_class_dict = {}
    # 遍历每一个视频目录
    for dir_name in one_path_dirs:
        abs_path = os.path.join(path, dir_name)
        abs_path_video_list = os.listdir(abs_path)
        # 为视频目录下每一个视频指定类别编号
        for video_name in abs_path_video_list:
            class_name = video_name.split("_")[1]
            video_class_dict[video_name] = class_dict.get(class_name)

    return video_class_dict


def specify_class_number(path):
    """
    为类别指定编号
    :return: 返回类别编号字典
    """
    # 获取根路径下的目录列表
    one_path = os.listdir(path)

    # 定义类别编号
    num = 0
    class_dict = {}
    for dir_name in one_path:
        class_dict[dir_name] = num
        num += 1

    return class_dict


if __name__ == "__main__":
    # 指定根目录
    one_path = "/Users/uxin/Desktop/zl_thesis/thesis_data/UCF-101"
    # 获取类别编号字典
    class_dict = specify_class_number(one_path)
    print(class_dict)
    # 为每个视频指定类别编号
    video_class_dict = specify_video_class(one_path, class_dict)
    print(video_class_dict)
























