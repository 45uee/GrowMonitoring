import cv2, base64, imutils, time, socket, os
import numpy as np


BUFF_SIZE = 65536
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFF_SIZE)
host_name = socket.gethostname()
host_ip = os.environ.get('PI_IP')
print(host_ip)

port = 9999
message = b'check'

client_socket.sendto(message, (host_ip, port))

while True:
    packet, _ = client_socket.recvfrom(BUFF_SIZE)
    data = base64.b64decode(packet, ' /')
    npdata = np.fromstring(data, dtype=np.uint8)
    frame = cv2.imdecode(npdata, 1)

    cv2.imshow("receive", frame)
    if cv2.waitKey(1) == ord('q'):
        client_socket.close()
        break