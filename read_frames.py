#!/usr/bin/env python3

from imutils.video import FPS
import numpy as np
import argparse
import imutils
import cv2
 
# open a pointer to the video stream and start the FPS timer
fps = FPS().start()

for i in range(1,99031):
    frame = cv2.imread('frames/' + str(i).zfill(6)+'.jpg')

    # display a piece of text to the frame (so we can benchmark
    # fairly against the fast method)
#    cv2.putText(frame, "Frame Method", (10, 30),
#            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
#    cv2.imshow("Frame", frame)
#    cv2.waitKey(1)

    fps.update()

#    if i % 1000 == 0:
#        fps.stop()
#        print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
print("[INFO] num frames: {:2d}".format(fps._numFrames))
 
#cv2.destroyAllWindows()
