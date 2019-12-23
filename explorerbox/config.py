import json
from collections import namedtuple

class Config:
	reset: bool
	window_width: int
	window_height: int
	depth_mm_min:int
	depth_mm_max:int
	depth_mm_threshold_diff:int
	depth_px_qty_ignore:int
	depth_frame_rate:float
	depth_posterize_qty:int
	picture_path:str
	picture_frequency:int
	border_top:int
	border_right:int
	border_bottom:int
	border_left:int
	color_map:str

	def __init__(self):
		self.reset=False
		self.window_width = 640
		self.window_height = 480
		self.depth_mm_min = 1010
		self.depth_mm_max = 1330
		self.depth_mm_threshold_diff = 40
		self.depth_px_qty_ignore = 11000
		self.depth_frame_rate = 0.25
		self.depth_posterize_qty = 15
		self.picture_path='config/sandbox.jpg'
		self.picture_frequency=0
		self.border_top=0
		self.border_right=0
		self.border_bottom=0
		self.border_left=0
		self.color_map='default'

	def loadFromFile(self):
		print('load config file', flush=True)
		self.reset=True
		with open('config/config.json', 'r') as cfg_file:
			data = json.load(cfg_file)
			self.window_width = data['window_width']
			self.window_height = data['window_height']
			self.depth_mm_min = data['depth_mm_min']
			self.depth_mm_max = data['depth_mm_max']
			self.depth_mm_threshold_diff = data['depth_mm_threshold_diff']
			self.depth_px_qty_ignore = data['depth_px_qty_ignore']
			self.depth_frame_rate = data['depth_frame_rate']
			self.depth_posterize_qty = data['depth_posterize_qty']
			self.picture_path = data['picture_path']
			self.picture_frequency = data['picture_frequency']
			self.border_top = data['border_top']
			self.border_right=data['border_right']
			self.border_bottom=data['border_bottom']
			self.border_left=data['border_left']
			self.color_map=data['color_map']