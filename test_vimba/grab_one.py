from vimba import Camera, Vimba, Frame
from vimba import *
import numpy as np
import cv2
import time
import scipy.ndimage as ndimage

class VimbaCamera:
    def __init__(self, sn):
        self.sn = sn
        self.camera: Camera = None
        self.frames = []

    def open(self):
        pass

    def close(self):
        pass

    def grab_one(self) -> Frame:
        
        with Vimba.get_instance() as vimba:
            with vimba.get_camera_by_id(self.sn) as cam:
                frame = cam.get_frame()
                return frame

if __name__ == "__main__":
    cam = VimbaCamera('0143K')
    cam.open()
    img = np.zeros((2056, 2464), dtype=np.uint16)
    n = 10
    for i in range(n):
        frame = cam.grab_one()
        f = frame.as_numpy_ndarray()
        f = f.squeeze()
        f = f[900:1100, 1100:1300]
        print("========================")
        print(f.shape, f.mean(), f.std())
        f = ndimage.gaussian_filter(f, sigma=(0.125, 0.125), order=0)
        print(f.shape, f.mean(), f.std())
        # img = img + f
        # print(img.max())

    img = img / n
    img = img.astype(np.uint8)
    cv2.imwrite(f'frame_avg{n}.png', img)
