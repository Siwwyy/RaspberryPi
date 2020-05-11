import P3picam_Python3
import picamera
from datetime import datetime
from subprocess import call


motion_state = False
motion_counter = 0;
file_path = "./CAPTURED/"

def Capture_Image(current_time, picture_path):
    # generate picture's name
    picture_name = current_time.strftime("%Y.%m.%d-%H:%M:%S" + '.jpg')
    with picamera.PiCamera() as camera:
        camera.resolution = (1280,720)
        camera.capture(picture_path + picture_name)
    print("We have taken a picture")
    return picture_name
    

def Get_Time():
    #fetch the current time
    current_time = datetime.now()
    return current_time


def Time_Stamp(current_time, picture_path, picture_name):
    #whole file path
    file_path = picture_path + picture_name
    # create message to stamp on picture
    message = current_time.strftime("%Y.%m.%d-%H%M%S")
    # create command to execute
    time_stamp_command = "/usr/bin/convert " + file_path + " -pointsize 36 -fill red -annotate +700+650 '" + message + "' " + file_path
    #execute the command
    call([time_stamp_command],shell=True)
    print("We have timestamped our picture!")
    

while True:
    motion_state = P3picam_Python3.motion()
    #print(motion_state)
    if motion_state == True:
        print("Motion detected")
        current_time = Get_Time()
        picture_name = Capture_Image(current_time, file_path)
        Time_Stamp(current_time,file_path,picture_name)
#        with picamera.PiCamera() as camera:
##            motion_file_path = "./CAPTURED/motion"+str(motion_counter)+".jpg"
#            camera.resolution = (1280,720)
#            camera.capture(motion_file_path)
#            motion_counter += 1
            
 