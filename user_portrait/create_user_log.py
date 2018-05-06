# #!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : create_user_log.py
# @Author: ZL
# @Date  : 2018/4/26
# @Desc  : 模拟服务端生成用户行为日志：
#               格式：{"uid":"1","videoType":"2","videoId":"car003","viewTime":"180s","datatime":"2018-04-26 09:55:08"}


import os
import random
import json
import io

import datetime

import specify_video_class


def create_user_records(user_info_dict, write_file_path, class_videos_dict):

    f = io.open(file=write_file_path, mode="a", encoding="utf-8")

    # 生成主要兴趣爱好的观看行为记录
    rate_list = [100, 80, 110]
    for i in user_info_dict:
        for main_type in range(rate_list[int(i) - 1]):
            # {"uid":"1","videoType":"2","videoId":"car003","viewTime":"180s","datatime":"2018-04-26 09:55:08"}
            record_dict = {}
            record_dict["uid"] = i
            video_type = -1
            if int(i) == 1:
                video_type = 20
            elif int(i) == 2:
                video_type = 50
            else:
                video_type = 80

            record_dict["videoType"] = video_type
            # 获取指定类别下的视频列表
            specify_class_videos_list = class_videos_dict.get(video_type)
            class_videos_list_len = len(specify_class_videos_list)
            record_dict["videoId"] = specify_class_videos_list[random.randint(0, class_videos_list_len-1)]
            # 秒级别
            record_dict["viewTime"] = random.randint(10, 240)
            random_date_num = random.randint(0, 30)
            random_date = datetime.datetime.now() - datetime.timedelta(days=random_date_num,
                                                                       hours=random_date_num,
                                                                       minutes=random_date_num)
            record_dict["datetime"] = str(datetime.datetime(random_date.year, random_date.month, random_date.day,
                                                            random_date.hour, random_date.minute, random_date.second))
            record_json = json.dumps(record_dict)
            f.write(record_json)
            f.write(os.linesep)

        # 生成随意的观看行为日志
        user_random_cnt = random.randint(100, 200)
        for i in range(user_random_cnt):
            record_dict = {}
            record_dict["uid"] = i
            video_type = random.randint(0, 100)
            record_dict["videoType"] = video_type
            # 获取指定类别下的视频列表
            specify_class_videos_list = class_videos_dict.get(video_type)
            if specify_class_videos_list is None:
                print(video_type)
            class_videos_list_len = len(specify_class_videos_list)
            record_dict["videoId"] = specify_class_videos_list[random.randint(0, class_videos_list_len)-1]
            # 秒级别
            record_dict["viewTime"] = random.randint(10, 240)
            random_date_num = random.randint(0, 30)
            random_date = datetime.datetime.now() - datetime.timedelta(days=random_date_num,
                                                                       hours=random_date_num,
                                                                       minutes=random_date_num)
            record_dict["datetime"] = str(datetime.datetime(random_date.year, random_date.month, random_date.day,
                                                            random_date.hour, random_date.minute, random_date.second))
            record_json = json.dumps(record_dict)
            f.write(record_json)
            f.write(os.linesep)

    f.close()


if __name__ == "__main__":

    # 指定根目录
    one_path = "/Users/uxin/Desktop/zl_thesis/thesis_data/UCF-101"

    # 获取类别编号字典
    class_dict = specify_video_class.specify_class_number(one_path)

    # 为每个视频指定类别编号
    video_class_dict = specify_video_class.specify_video_class(one_path, class_dict)

    # 创建每一类别下所有视频的记录字典
    # 格式：{0:[video1,video2,...],....}
    class_videos_dict = {}
    for k in video_class_dict:
        v = video_class_dict.get(k)
        if v in class_videos_dict:
            class_videos_dict[v].append(k)
        else:
            videos_list = []
            videos_list.append(k)
            class_videos_dict[v] = videos_list
    # 创建用户的行为记录
    user_records_file_path = "/Users/uxin/Desktop/zl_thesis/thesis_data/user_action_records.txt"
    # 1=男，0=女
    user_info_dict = {
        "1": {"name": "tom", "sex": "1"},  # 喜欢20类型
        "2": {"name": "jerry", "sex": "0"},  # 喜欢50类型
        "3": {"name": "tomas", "sex": "1"}  # 喜欢80类型
    }
    create_user_records(user_info_dict, user_records_file_path, class_videos_dict)
