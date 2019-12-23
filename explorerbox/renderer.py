import cv2
import numpy as np

class Renderer:
    def __init__(self, config):
        self.config = config
        
        # taken from pyqtgraph GradientEditorItem
        self.cmaps={           
            "default":(
                (0, (100, 5, 200)),
                (0.05, (0, 0, 255)),
                (0.5, (0, 255, 0)),
                (0.6, (255, 200, 0)),
                (0.99, (255, 0, 0)),
                (1.0, (255, 255, 255))
            ),
            "inverted":(
                (0, (255, 255, 255)),
                (0.05, (255, 0, 0)),                
                (0.5, (255, 200, 0)),
                (0.6, (0, 255, 0)),
                (0.99, (0, 0, 255)),
                (1.0, (100, 5, 200))
            ),
            "darkmode":(
                (0, (100, 2, 180)),
                (0.05, (0, 0, 200)),
                (0.5, (0, 180, 0)),
                (0.6, (200, 180, 0)),
                (0.99, (200, 0, 0)),
                (1.0, (200, 200, 200))
            ),
            "rainbow":(
                (0, (255, 0, 0)),
                (0.16, (255, 127, 0)),
                (0.33, (255, 255, 0)),
                (0.5, (0, 255, 0)),
                (0.66, (0, 0, 255)),
                (0.83, (46, 43, 95)),
                (1.0, (139, 0, 255))
            )
        }

    def execute(self, depth_image):
        depth_image = self.interpolate(depth_image)
        depth_image = self.resize(depth_image)        
        depth_image = self.invert(depth_image)
        tmp_posterize= self.posterize(depth_image, self.config.depth_posterize_qty)

        if self.config.enable_posterize:
            poster_image = tmp_posterize
        else:
            poster_image = depth_image

        color_image = self.colorize(np.copy(poster_image)) 
        color_image = self.blur(color_image)

        if self.config.enable_contourize:
            self.contourize(color_image, tmp_posterize)
        self.borderize(color_image)
        return color_image

    def borderize(self, im):
        height, width, channels = im.shape
        for x in range(0,width):
            for y in range(0,height):
                if x < self.config.border_left or y < self.config.border_top or x > (width - self.config.border_right) or y > (height - self.config.border_bottom):
                    im[y,x] = [0,0,0]

    def interpolate(self, im):
        return np.interp(im,(self.config.depth_mm_min,self.config.depth_mm_max),(0,255)).astype(np.uint8) 

    def resize(self, im):
        return cv2.resize(im, (self.config.window_width, self.config.window_height))  

    def invert(self, im):
        return 255 - im

    def blur(self, im):
        return cv2.GaussianBlur(im,(5,5),0)

    def posterize(self, im, n):
        indices = np.arange(0,256)   # List of all colors 
        divider = np.linspace(0,255,n+1)[1] # we get a divider
        quantiz = np.int0(np.linspace(0,255,n)) # we get quantization colors
        color_levels = np.clip(np.int0(indices/divider),0,n-1) # color levels 0,1,2..
        palette = quantiz[color_levels] # Creating the palette
        im2 = palette[im]  # Applying palette on image
        im2 = cv2.convertScaleAbs(im2) # Converting image back to uint8
        return im2

    def colorize(self, im):
        mx = 256  # if gray.dtype==np.uint8 else 65535
        lut = np.empty(shape=(256, 3))

        if self.config.color_map in self.cmaps:
            cmap = self.cmaps[self.config.color_map]
        else:
            cmap = self.cmaps["default"]
        
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

    def contourize(self, im, src):
        thresh = cv2.adaptiveThreshold(src,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,3,0)
        contours, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(im, contours, -1, (50,50,50), 1)
