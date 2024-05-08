import cv2
import numpy as np
from utils import plant, light_intensity

frame = cv2.imread('frame.jpg')

if __name__ == '__main__':
    
    print("Plant area: ", plant.plant_area(frame))
    print("Plant ratio: ", plant.plant_ratio(frame))
    print("Light: ", light_intensity.light_intensity(frame))

    cv2.imshow('mask', plant.plant_mask(frame))
    cv2.waitKey(0)
    cv2.destroyAllWindows()