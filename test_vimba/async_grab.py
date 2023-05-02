import sys
from typing import Optional, Tuple
from vimba import *


def print_preamble():
    print('///////////////////////////////////////////')
    print('/// Vimba API Asynchronous Grab Example ///')
    print('///////////////////////////////////////////\n')


def print_usage():
    print('Usage:')
    print('    python asynchronous_grab.py [/x] [-x] [camera_id]')
    print('    python asynchronous_grab.py [/h] [-h]')
    print()
    print('Parameters:')
    print('    /x, -x      If set, use AllocAndAnnounce mode of buffer allocation')
    print('    camera_id   ID of the camera to use (using first camera if not specified)')
    print()


def abort(reason: str, return_code: int = 1, usage: bool = False):
    print(reason + '\n')

    if usage:
        print_usage()

    sys.exit(return_code)


def parse_args() -> Tuple[Optional[str], AllocationMode]:
    args = sys.argv[1:]
    argc = len(args)

    allocation_mode = AllocationMode.AnnounceFrame
    cam_id = ""
    for arg in args:
        if arg in ('/h', '-h'):
            print_usage()
            sys.exit(0)
        elif arg in ('/x', '-x'):
            allocation_mode = AllocationMode.AllocAndAnnounceFrame
        elif not cam_id:
            cam_id = arg

    if argc > 2:
        abort(reason="Invalid number of arguments. Abort.", return_code=2, usage=True)

    return (cam_id if cam_id else None, allocation_mode)


def get_camera(camera_id: Optional[str]) -> Camera:
    with Vimba.get_instance() as vimba:
        if camera_id:
            try:
                return vimba.get_camera_by_id(camera_id)

            except VimbaCameraError:
                abort('Failed to access Camera \'{}\'. Abort.'.format(camera_id))

        else:
            cams = vimba.get_all_cameras()
            if not cams:
                abort('No Cameras accessible. Abort.')

            return cams[0]


def setup_camera(cam: Camera):
    with cam:
        # Try to adjust GeV packet size. This Feature is only available for GigE - Cameras.
        try:
            cam.GVSPAdjustPacketSize.run()

            while not cam.GVSPAdjustPacketSize.is_done():
                pass

        except (AttributeError, VimbaFeatureError):
            pass


def frame_handler(cam: Camera, frame: Frame):
    print('{} acquired {}'.format(cam, frame), flush=True)

    cam.queue_frame(frame)


def main():
    print_preamble()
    cam_id, allocation_mode = parse_args()

    with Vimba.get_instance():
        with get_camera(cam_id) as cam:

            setup_camera(cam)
            print('Press <enter> to stop Frame acquisition.')

            try:
                # Start Streaming with a custom a buffer of 10 Frames (defaults to 5)
                cam.start_streaming(handler=frame_handler, buffer_count=10, allocation_mode=allocation_mode)
                input()

            finally:
                cam.stop_streaming()


if __name__ == '__main__':
    main()