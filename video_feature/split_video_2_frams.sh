#! /usr/bin/bash

cd /Users/uxin/Desktop/张磊本科毕业论文/thesis_data/UCF-101

# 遍历视频文件夹
for forder in `ls`; 
	do 	
		cd `pwd`/${forder};
		echo "进入"${forder}"文件夹"
		# 对每一个视频进行帧切割处理
		for file in `ls`; 
			do 	echo ${file} "start video split to frame";
				mkdir -p ../../split_frams/${forder}/${file%.*};
				#ffmpeg -i `pwd`/${file} -s 300x300 -r 30 ../../split_frams/${forder}/${file%.*}/%06d.jpg;
				ffmpeg -i `pwd`/${file} ../../split_frams/${forder}/${file%.*}/%06d.jpg;
		done
		cd .. ;
done



















