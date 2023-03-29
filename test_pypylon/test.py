import os
import numpy
from PIL import Image

num = 3
os.environ["PYLON_CAMEMU"] = "%d" % num
from pypylon import pylon

def get_class_and_filter():
    device_class = "BaslerCamEmu"
    di = pylon.DeviceInfo()
    di.SetDeviceClass(device_class)
    return device_class, [di]


class PylonEmuTestCase:
    num_dev = num
    device_class, device_filter = get_class_and_filter()

    def create_first(self):
        tlf = pylon.TlFactory.GetInstance()
        return pylon.InstantCamera(tlf.CreateFirstDevice(self.device_filter[0]))

class GrabTestSuite(PylonEmuTestCase):
    def test_grabone(self):

        camera = self.create_first()
        camera.Open()
        camera.ExposureTimeAbs.SetValue(10000.0)
        result = camera.GrabOne(1000)
        img = Image.fromarray(result.Array)
        img.save("grab.png")
        camera.Close()

    def test_grab(self):
        countOfImagesToGrab = 5
        imageCounter = 0
        camera = self.create_first()
        camera.Open()
        camera.ExposureTimeAbs.SetValue(20000.0)
        camera.StartGrabbingMax(countOfImagesToGrab)
        # Camera.StopGrabbing() is called automatically by the RetrieveResult() method
        # when c_countOfImagesToGrab images have been retrieved.
        while camera.IsGrabbing():
            # Wait for an image and then retrieve it. A timeout of 5000 ms is used.
            grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
            # Image grabbed successfully?
            if grabResult.GrabSucceeded():
                # Access the image data.
                imageCounter = imageCounter + 1
                img = Image.fromarray(grabResult.Array)
                img.save(f"grabbing{imageCounter}.png")

            grabResult.Release()
        camera.Close()

if __name__ == "__main__":
    test = GrabTestSuite()
    test.test_grabone()
    test.test_grab()