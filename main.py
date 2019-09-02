import sandbox as sb
import kinect as ki
import config as cfg
import renderer as rd
import cv2

def main():
	cv2.namedWindow('sandbox')
	
	config = cfg.Config()		
	sandbox = sb.Sandbox(config, ki.Kinect(), rd.Renderer(config))
	sandbox.execute()
	
	cv2.destroyAllWindows()

main()
