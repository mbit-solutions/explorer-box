import sandbox as sb
import kinect as ki
import config as cfg
import cv2

def main():
	cv2.namedWindow('sandbox')
	
	config = cfg.Config()	
	sandbox = sb.Sandbox(config, ki.Kinect())
	sandbox.execute()
	
	cv2.destroyAllWindows()

main()
