import picamera


#setup the camera such that it closes
#when we are done with it

with picamera.PiCamera() as camera:
    camera.resolution = (1280,720) #HD resolution
    camera.capture("./CAPTURES/img.jpg")