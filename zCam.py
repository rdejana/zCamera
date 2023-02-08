import zmq
import cv2
import numpy as np

def recv_image(socket, dtype, shape):
    data = socket.recv()
    buf = memoryview(data)
    array = np.frombuffer(buf, dtype=dtype)
    return array.reshape(shape)

# 1807
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.setsockopt(zmq.CONFLATE, 1)  # last msg only.
socket.setsockopt(zmq.SUBSCRIBE, b'') # all topics
socket.connect("tcp://192.168.1.6:%d" % 1807)
image_shape = (224, 224, 3)
image_dtype = np.uint8
while(True):
    image = recv_image(socket, image_dtype, image_shape)
    cv2.imshow('frame', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print("all done")