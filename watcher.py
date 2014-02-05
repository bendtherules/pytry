import sys
import time
import subprocess
import os
dir_to_watch=r"E:\Babu\pytry\robocon"
file_to_watch=r"robo1.js.text"
full_path=os.path.join(dir_to_watch,file_to_watch)
def build_cmd():
    a,b= subprocess.Popen(r'slideshow build '+file_to_watch+' -t impress.js', shell=True,cwd=dir_to_watch, stderr=subprocess.PIPE, stdout=subprocess.PIPE ).communicate()
    return a
from watchdog.observers import Observer
from watchdog.tricks import LoggerTrick
import watchdog

print("Watching file "+full_path+" for any changes.. Dont close")

class rebuild(watchdog.events.FileSystemEventHandler):
    def on_any_event(self,event):
        if event.src_path==full_path:
            print("Re-building")
            print(build_cmd())

event_handler = rebuild()
observer = Observer()
observer.schedule(event_handler, dir_to_watch, recursive=True)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()

