import cv2
import numpy as np

def colorize( im ):
    return cv2.applyColorMap(im,cv2.COLORMAP_JET)
    
def explorer_colorize( im ):
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
