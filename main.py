import sys
import sandbox as sb
import config as cfg
import renderer as rd
import Tkinter

fake_mode = False
calibrate_beamer_mode = False
calibrate_kinect_mode = False

if len(sys.argv) == 2 and sys.argv[1] == 'fakenect':
    fake_mode = True

if len(sys.argv) == 2 and sys.argv[1] == 'beamer_calibrate':
    calibrate_beamer_mode = True
    fake_mode = True

if len(sys.argv) == 2 and sys.argv[1] == 'kinect_calibrate':
    calibrate_kinect_mode = True
    fake_mode = True

if fake_mode == True:
    import fakenect as fa
    nect = fa.Fakenect()
else:
    import kinect as ki
    nect = ki.Kinect()

window = Tkinter.Tk()
window.attributes('-fullscreen', True)
window.bind('<Escape>',lambda e: window.destroy())

config = cfg.Config()
sandbox = sb.Sandbox(config, nect, rd.Renderer(config))

if calibrate_beamer_mode == True:
    sandbox.calibrate_beamer(window)
elif calibrate_kinect_mode == True:
    sandbox.calibrate_kinect(window)
else:
    sandbox.execute(window)