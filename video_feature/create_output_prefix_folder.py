# #!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : create_output_prefix_folder.py
# @Author: ZL
# @Date  : 2018/5/5
# @Desc  : 创建视频特征输出目录

import os


def create_video_feature_folder(one_path):
    # 类别目录名列表
    one_path_dirs_list = os.listdir(one_path)

    for dir_name in one_path_dirs_list:
        video_class_path = os.path.join(one_path, dir_name)

        # 获取指定类别视频下的所有视频名列表
        specify_class_videos_name_list = os.listdir(video_class_path)

        # 特征输出目录
        video_feature_dir = video_class_path.replace("UCF-101", "video_feature")
        os.mkdir(video_feature_dir)

        for video_name in specify_class_videos_name_list:
            video_name = video_name.split(".")[0]

            # 获取视频目录路径
            video_path = os.path.join(video_feature_dir, video_name)

            # 创建特征输出目录
            os.mkdir(video_path)


if __name__ == "__main__":

    one_path = "/Users/uxin/Desktop/zl_thesis/thesis_data/UCF-101"

    # 创建视频特征输出目录
    create_video_feature_folder(one_path)





