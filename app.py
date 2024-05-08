import cv2
import numpy as np
from utils import plant_measurements, env_measurements
from picamera2 import Picamera2
import time


def define_picam():
    picam2 = Picamera2()
    picam2.preview_configuration.main.size = (1920, 1080)
    picam2.preview_configuration.main.format = "RGB888"
    picam2.preview_configuration.controls.FrameRate = 60
    picam2.preview_configuration.align()

    #picam2.configure(picam2.create_preview_configuration(main={"format": 'RGB888', "size": (640, 480)}))
    return picam2


if __name__ == '__main__':
    picam2 = define_picam()
    picam2.start()

    frame = picam2.capture_array()

    print("Plant area: ", plant_measurements.plant_area(frame))
    print("Plant ratio: ", plant_measurements.plant_ratio(frame))
    print("Light intensity: ", env_measurements.light_intensity(frame))

    cv2.imwrite(f"/home/user/img/{time.time()}_img.jpg", frame)
