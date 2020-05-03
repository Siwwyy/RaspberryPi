import picamera
from time import sleep
from subprocess import call #linux commands in python


#Setup the camera
with picamera.PiCamera() as camera:
    camera.start_recording("./CAPTURES/video.h264")
    sleep(5)
    camera.stop_recording()
    
#camera is now closed
    
print("We are going to convert the video")
#define the command we want
command = "MP4Box -add ./CAPTURES/video.h264 ./CAPTURES/converted_video.mp4"
#execute command above
call([command],shell=True)
#Video converted
print("Video converted")