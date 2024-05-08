import cv2


def plant_mask(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_green = (20, 40, 40)
    upper_green = (160, 255, 255)
    mask = cv2.inRange(hsv, lower_green, upper_green)
    return mask

def plant_area(frame):
    mask = plant_mask(frame)
    return cv2.countNonZero(mask)

def plant_ratio(frame):
    mask = plant_mask(frame)
    total_pixels = frame.shape[0] * frame.shape[1]
    return cv2.countNonZero(mask) / total_pixels

'''def plant_height(frame):
    mask = plant_mask(frame)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) == 0:
        return 0
    return max(contours, key=cv2.contourArea)'''
