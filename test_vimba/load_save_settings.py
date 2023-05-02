from vimba import Camera, Vimba, Frame
from vimba import *
import numpy as np
import cv2

class VimbaCamera:
    def __init__(self, sn):
        self.sn = sn
        self.camera: Camera = None
        self.frames = []

    def open(self):
        pass

    def close(self):
        pass

    def load_save_settings(self) -> Frame:
        
        with Vimba.get_instance() as vimba:
            with vimba.get_camera_by_id(self.sn) as cam:
                settings_file = "settings.xml"
                cam.save_settings(settings_file, PersistType.All)

                try:
                    cam.UserSetSelector.set('Default')
                except (AttributeError, VimbaFeatureError):
                    print("failed")

                try:
                    cam.UserSetLoad.run()
                except (AttributeError, VimbaFeatureError):
                    print("failed 2")

                cam.load_settings(settings_file, PersistType.All)


if __name__ == "__main__":
    cam = VimbaCamera('0143K')
    cam.load_save_settings()
