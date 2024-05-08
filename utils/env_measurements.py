import numpy as np
import cv2

def light_intensity(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return np.mean(gray)