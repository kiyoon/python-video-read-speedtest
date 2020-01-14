# Python video reading speed test

This project measures reading speed depending on the video format (i.e. frame images vs a long video vs many short videos) using Python OpenCV. This is mainly designed for measuring deep learning video dataloader efficiency, because many researchers tend to extract frames from videos rather than loading video files directly.

Additionally, this experiment shows whether using HDD during training is feasible or not. Reading speed of video files is not much different between SSD and HDD.

## Results

We ran the same code twice to test also the filesystem cache effect. The more file it accesses, the bigger the difference between the two runs.

### Samsung 860 EVO SSD

* Reading image frames:  

```bash
$ echo 3 | sudo tee /proc/sys/vm/drop_caches
$ ./read_frames.py 
[INFO] elasped time: 64.29
[INFO] approx. FPS: 1540.27
[INFO] num frames: 99030

$ ./read_frames.py
[INFO] elasped time: 51.65
[INFO] approx. FPS: 1917.34
[INFO] num frames: 99030
```

* Reading a long video:  

```bash
$ echo 3 | sudo tee /proc/sys/vm/drop_caches
$ ./read_video.py
[INFO] elasped time: 8.70
[INFO] approx. FPS: 11384.37
[INFO] num frames: 99030

$ ./read_video.py 
[INFO] elasped time: 8.76
[INFO] approx. FPS: 11307.68
[INFO] num frames: 99030
```

* Reading many short (3s) videos:  

```bash
$ echo 3 | sudo tee /proc/sys/vm/drop_caches
$ ./read_video_chunks.py 
[INFO] elasped time: 10.09
[INFO] approx. FPS: 9811.59
[INFO] num frames: 99030

$ ./read_video_chunks.py
[INFO] elasped time: 9.91
[INFO] approx. FPS: 9988.92
[INFO] num frames: 99030
```

### Toshiba DT01ACA300 HDD

* Reading image frames:  

```bash
$ echo 3 | sudo tee /proc/sys/vm/drop_caches
$ ./read_frames.py 
[INFO] elasped time: 94.82
[INFO] approx. FPS: 1044.35
[INFO] num frames: 99030

$ ./read_frames.py 
[INFO] elasped time: 51.59
[INFO] approx. FPS: 1919.47
[INFO] num frames: 99030
```

* Reading a long video:  

```bash
$ echo 3 | sudo tee /proc/sys/vm/drop_caches
$ ./read_video.py
[INFO] elasped time: 8.87
[INFO] approx. FPS: 11164.87
[INFO] num frames: 99030

$ ./read_video.py
[INFO] elasped time: 8.72
[INFO] approx. FPS: 11352.42
[INFO] num frames: 99030
```

* Reading many short (3s) videos:  

```bash
$ echo 3 | sudo tee /proc/sys/vm/drop_caches
$ ./read_video_chunks.py 
[INFO] elasped time: 10.41
[INFO] approx. FPS: 9511.57
[INFO] num frames: 99030

$ ./read_video_chunks.py 
[INFO] elasped time: 9.92
[INFO] approx. FPS: 9978.48
[INFO] num frames: 99030
```

# Usage

## Dependencies

### System
ffmpeg

### Python3
imutil  
opencv  
opencv-contrib-python

## Scripts

* Download a sample video (one sample from the EPIC-Kitchens dataset)  
`$ ./download_video.sh`

* Measure image frames reading speed:  
```bash
$ ./extract_video_frame.sh
$ ./read_frames.py
```

* Measure long video reading speed:  
```bash
$ ./rescale_video.sh
$ ./read_video.py
```

* Measure short videos reading speed:  
```bash
$ ./rescale_video_chunk.sh
$ ./read_video_chunks.py
```

* If you want to run again, consider removing disk cache:  
`$ echo 3 | sudo tee /proc/sys/vm/drop_caches`