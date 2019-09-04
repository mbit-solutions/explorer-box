import freenect as fn

class Kinect:
    def get_depth_image_mm(self):
        return fn.sync_get_depth(0, fn.DEPTH_MM)[0]
    
    def get_video(self):
        return fn.sync_get_video()[0]