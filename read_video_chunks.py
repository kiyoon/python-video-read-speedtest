#!/usr/bin/env python3

from imutils.video import FPS
import numpy as np
import imutils
import cv2
 
# open a pointer to the video stream and start the FPS timer
fps = FPS().start()

# loop over frames from the video file stream
for i in range(398):
    stream = cv2.VideoCapture('chunks/' + str(i).zfill(6)+'.mp4')
    while True:
        # grab the frame from the threaded video file stream
        (grabbed, frame) = stream.read()

        # if the frame was not grabbed, then we have reached the end
        # of the stream
        if not grabbed:
            break

        # display a piece of text to the frame (so we can benchmark
        # fairly against the fast method)
#        cv2.putText(frame, "Chunk Method", (10, 30),
#                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        # show the frame and update the FPS counter
#        cv2.imshow("Frame", frame)
#        cv2.waitKey(1)
        fps.update()
    stream.release()
#    fps.stop()
#    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
print("[INFO] num frames: {:2d}".format(fps._numFrames))
 
# do a bit of cleanup
#cv2.destroyAllWindows()
