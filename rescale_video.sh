#!/bin/bash

ffmpeg -i "P01_01.MP4" -vf scale=224:224:flags=bicubic,setdar=1/1 -c:v libx264 -preset fast -crf 22 -an rescaled.mp4
