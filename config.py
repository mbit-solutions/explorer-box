import cv2

class Config:
	def __init__(self):
		self.window_width = 640
		self.window_height = 480
		self.depth_mm_min = 1000
		self.depth_mm_max = 1200
		self.depth_mm_threshold_diff = 40
		self.depth_px_qty_ignore = 12000	
		self.depth_frame_rate = 0.25	
