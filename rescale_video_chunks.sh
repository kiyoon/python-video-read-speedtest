#!/bin/bash

mkdir chunks
ffmpeg -i "P01_01.MP4" -vf scale=224:224:flags=bicubic,setdar=1/1 -c:v libx264 -preset fast -crf 22 -an -map 0 -segment_time 00:00:03 -f segment -reset_timestamps 1 chunks/%06d.mp4
