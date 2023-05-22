from pathlib import Path

import cv2
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    video = Path(".") / "tests" / "images" / "seq07.mp4"

    # load the videocapture element
    cap = cv2.VideoCapture(str(video))
    frame_buffer = []
    # Initiate ORB detector
    orb = cv2.ORB_create()
    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    while True:
        ret, frame = cap.read()
        if ret == False:
            break
        if len(frame_buffer) == 2:
            # matcher logic
            img1 = cv2.cvtColor(frame_buffer[0], cv2.COLOR_BGR2GRAY)
            img2 = cv2.cvtColor(frame_buffer[1], cv2.COLOR_BGR2GRAY)
            # detect keypoints
            kp1, des1 = orb.detectAndCompute(img1, None)
            kp2, des2 = orb.detectAndCompute(img2, None)
            matches = bf.match(des1, des2)
            matches = sorted(matches, key=lambda x: x.distance)
            img3 = cv2.drawMatches(
                img1,
                kp1,
                img2,
                kp2,
                matches[:20],
                None,
                flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS,
            )
            cv2.imshow("matches", img3)
            cv2.waitKey(0)
            frame_buffer.pop(0)
        else:
            frame_buffer.append(frame)
