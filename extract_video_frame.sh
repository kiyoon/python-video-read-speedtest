#!/bin/bash

mkdir frames
ffmpeg -i "P01_01.MP4" -vf scale=224:224:flags=bicubic,setdar=1/1 -q:v 1 "frames/%06d.jpg"
