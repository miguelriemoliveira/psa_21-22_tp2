#!/usr/bin/env python3

# import the opencv library
import cv2

# --------------------------------
# Initialization
# --------------------------------
vid = cv2.VideoCapture(4) # define a video capture object

# --------------------------------
# Execution (in cycle)
# --------------------------------
while True:

    ret, image = vid.read() # Capture the video frame

    # Display the resulting frame
    cv2.imshow('frame', image)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# --------------------------------
# Termination
# --------------------------------
vid.release() # After the loop release the cap object
cv2.destroyAllWindows() # Destroy all the windows
