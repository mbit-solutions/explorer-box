import numpy as np
import cv2
import time
import PIL.Image
import PIL.ImageTk
import Tkinter


class Sandbox:
    def __init__(self, config, nect, renderer):
        self.config = config
        self.nect = nect
        self.renderer = renderer

    def get_depth_image_diff_mm(self, previous, current, threshold):
        p = previous.astype(np.int16)
        c = current.astype(np.int16)
        diff = c - p
        diff[np.where(diff < 0)] *= -1
        return np.where(diff > [threshold])

    def create_canvas(self, window):
        canvas = Tkinter.Canvas(
            window, width=self.config.window_width, height=self.config.window_height)
        canvas.pack()
        return canvas
    
    def update_canvas(self, canvas, window, im):
        photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(im))
        canvas.create_image(0, 0, image=photo, anchor=Tkinter.NW)
        window.update_idletasks()
        window.update()

    def execute(self, window):
        print('starting explorer box')
        print('creating canvas')
        canvas = self.create_canvas(window)

        print('getting depth images')
        original_depth = self.nect.get_depth_image_mm()
        previous_depth_reset = np.copy(original_depth)
        previous_depth = np.copy(original_depth)

        while True:
            original_depth = self.nect.get_depth_image_mm()
            current_depth = np.copy(original_depth)

            diff_coords = self.get_depth_image_diff_mm(
                previous_depth, current_depth, self.config.depth_mm_threshold_diff)
            current_depth[diff_coords] = previous_depth[diff_coords]

            coords_qty = len(np.where(original_depth < [
                             self.config.depth_mm_min])[0])

            if coords_qty < self.config.depth_px_qty_ignore:
                current_depth = original_depth
                previous_depth_reset = np.copy(current_depth)
            else:
                print('take previous depth image - ignore pixel quantity', coords_qty)
                c = np.where(current_depth < [self.config.depth_mm_min])
                current_depth[c] = previous_depth_reset[c]

            previous_depth = np.copy(current_depth)
            self.update_canvas(canvas, window, self.renderer.execute(current_depth))
            time.sleep(self.config.depth_frame_rate)

    def calibrate(self, window):
        
        im = np.zeros((self.config.window_height, self.config.window_width))        
        #im = np.pad(im, pad_width=5, mode='constant', constant_values=0)

        canvas = self.create_canvas(window)
        photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(im))        
        canvas.create_image(0, 0, image=photo, anchor=Tkinter.NW)
        window.mainloop()
