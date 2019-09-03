import numpy as np

class Fakenect:
    def get_depth_image_mm(self):
        im = np.random.randint(1000, 1310, (16,12))              
        im = np.kron(im, np.ones((40,40), int))
        return im