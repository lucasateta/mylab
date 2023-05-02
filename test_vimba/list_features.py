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

    def list_features(self) -> Frame:
        
        with Vimba.get_instance() as vimba:
            with vimba.get_camera_by_id(self.sn) as cam:
                for feature in cam.get_all_features():
                    self.print_feature(feature)

    def print_feature(self, feature):
        try:
            value = feature.get()

        except (AttributeError, VimbaFeatureError):
            value = None

        print('/// Feature name   : {}'.format(feature.get_name()))
        print('/// Display name   : {}'.format(feature.get_display_name()))
        print('/// Tooltip        : {}'.format(feature.get_tooltip()))
        print('/// Description    : {}'.format(feature.get_description()))
        print('/// SFNC Namespace : {}'.format(feature.get_sfnc_namespace()))
        print('/// Unit           : {}'.format(feature.get_unit()))
        print('/// Value          : {}\n'.format(str(value)))

if __name__ == "__main__":
    cam = VimbaCamera('0143K')
    cam.list_features()
