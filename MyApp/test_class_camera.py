#!/usr/bin/env python3

# import the opencv library
from ClassCamera import ClassCamera
import cv2

# --------------------------------
# Initialization
# --------------------------------

camera = ClassCamera()

camera.connect(4)

# --------------------------------
# Execution (in cycle)
# --------------------------------
while True:

    success = camera.getData()
    if success:
        cv2.imshow('frame', camera.image)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# --------------------------------
# Termination
# --------------------------------
camera.disconnect()
cv2.destroyAllWindows() # Destroy all the windows
