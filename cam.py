# libcamera-hello -t 0
import cv2
import base64
import numpy as np
from picamera2 import Picamera2
import socket, os


BUFF_SIZE = 65536
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFF_SIZE)
host_ip = os.environ.get('PI_IP')
port = 9999
socket_address = (host_ip, port)
server_socket.bind(socket_address)
print("Listening: ", socket_address)

def define_picam():
    picam2 = Picamera2()
    picam2.preview_configuration.main.size = (640, 640)
    picam2.preview_configuration.main.format = "RGB888"
    picam2.preview_configuration.controls.FrameRate = 60
    picam2.preview_configuration.align()


    #picam2.configure(picam2.create_preview_configuration(main={"format": 'RGB888', "size": (640, 480)}))
    return picam2


def cam_stream():
    while True:
        msg, client_addr = server_socket.recvfrom(BUFF_SIZE)
        print('Got connection from', client_addr)
        
        cam = define_picam()
        cam.start()
        
        while True:
            frame = cam.capture_array()
            
            encoded, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
            message = base64.b64encode(buffer)
            server_socket.sendto(message, client_addr)


        

if __name__ == "__main__":
    cam_stream()
    server_socket.close()