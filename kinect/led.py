import freenect
import time

def cb(dev, data, timestamp):		
	print(data)
	time.sleep(0.5)

ctx = freenect.init()
dev = freenect.open_device(ctx, 0)

freenect.set_led(dev, freenect.LED_GREEN)
freenect.set_tilt_degs(dev, 0)
time.sleep(2.5)

freenect.set_led(dev, freenect.LED_OFF)
#freenect.start_depth(dev)
#freenect.set_depth_callback(dev, cb)

#while True:
#	freenect.process_events(ctx)	

#freenect.stop_depth(dev)
freenect.close_device(dev)
freenect.shutdown(ctx)
