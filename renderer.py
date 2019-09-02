import cv2
import numpy as np

class Renderer:
    def __init__(self, config)
        self.config = config

    def execute(depth_image):
        depth_image = interpolate(depth_image)
        depth_image = resize(depth_image)
        depth_image = invert(depth_image)
        poster_image = poster_image(depth_image, 10)
        color_image = colorize(np.copy(poster_image)) 
        color_image = blur(color_image)
        contourize(color_image, poster_image)
        return color_image

    def interpolate(im):
        return np.interp(im,(self.config.depth_mm_min,self.config.depth_mm_max),(0,255)).astype(np.uint8) 

    def resize(im):
        return cv2.resize(im, (self.config.window_width, self.config.window_height))  

    def invert(im):
        return 255 - im

    def blur(im):
        return cv2.GaussianBlur(im,(3,3),0)

    def posterize(im, n):
        indices = np.arange(0,256)   # List of all colors 
        divider = np.linspace(0,255,n+1)[1] # we get a divider
        quantiz = np.int0(np.linspace(0,255,n)) # we get quantization colors
        color_levels = np.clip(np.int0(indices/divider),0,n-1) # color levels 0,1,2..
        palette = quantiz[color_levels] # Creating the palette
        im2 = palette[im]  # Applying palette on image
        im2 = cv2.convertScaleAbs(im2) # Converting image back to uint8
        return im2

    def colorize(im):
        mx = 256  # if gray.dtype==np.uint8 else 65535
        lut = np.empty(shape=(256, 3))
        cmap = (
            # taken from pyqtgraph GradientEditorItem
            (0, (250, 5, 100)),
            (0.05, (255, 0, 0)),
            (0.4, (0, 255, 0)),
            (0.5, (0, 200, 255)),
            (0.99, (0, 0, 255)),
            (1.0, (255, 255, 255))
        )
        # build lookup table:
        lastval, lastcol = cmap[0]
        for step, col in cmap[1:]:
            val = int(step * mx)
            for i in range(3):
                lut[lastval:val, i] = np.linspace(
                    lastcol[i], col[i], val - lastval)

            lastcol = col
            lastval = val

        s0, s1 = im.shape
        out = np.empty(shape=(s0, s1, 3), dtype=np.uint8)

        for i in range(3):
            out[..., i] = cv2.LUT(im, lut[:, i])
        
        return out

    def contourize( im, src ):
        thresh = cv2.adaptiveThreshold(src,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,3,0)
        _, contours, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(im, contours, -1, (0,0,0), 1)
