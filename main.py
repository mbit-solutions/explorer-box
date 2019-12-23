import sys
import time
import tkinter
from explorerbox import sandbox as sb
from explorerbox import config as cfg
from explorerbox import renderer as rd
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

config = cfg.Config()
config.loadFromFile()

class ConfigChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == 'config/config.json':
            print('detected change in configfile')
            config.loadFromFile()

def main():
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

    if fake_mode == True:
        from kinect import fakenect as fa
        nect = fa.Fakenect()
    else:
        from kinect import kinect as ki
        nect = ki.Kinect()
        
    window = tkinter.Tk()
    window.attributes('-fullscreen', True)
    window.bind('<Escape>',lambda e: window.destroy())
    sandbox = sb.Sandbox(config, nect, rd.Renderer(config))

    if calibrate_beamer_mode == True:
        sandbox.calibrate_beamer(window)
    elif calibrate_kinect_mode == True:
        sandbox.calibrate_kinect(window)
    else:
        sandbox.execute(window)

if __name__ == '__main__':
    event_handler = ConfigChangeHandler()
    observer=Observer()
    observer.schedule(event_handler,path='config/',recursive=False)
    observer.start()
    main()