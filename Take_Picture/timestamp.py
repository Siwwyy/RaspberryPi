import picamera
from subprocess import call
from datetime import datetime
from time import sleep



#our file path
file_path = "/home/pi/Desktop/Python_PROJECTS/Pi_Camera/TUTORIAL/Take_Picture/CAPTURES/TimeStamped_Pics/"
picture_counter = 0
picture_total = 5

while picture_counter < picture_total:
    #Grab the current time
    current_time = datetime.now()
    picture_time = current_time.strftime("%Y.%m.%d-%H:%M:%S")
    picture_name = picture_time + '.jpg'
    whole_file_path = file_path + picture_name


    #take the picture using new file path
    with picamera.PiCamera() as camera:
        camera.resolution = (1280,720)
        camera.capture(whole_file_path)
        print("We have taken a picture")
        
    #create our time stamp variables
    timestamp_message = picture_time
    timestamp_command = "/usr/bin/convert " + whole_file_path + " -pointsize 36 -fill red -annotate +700+650 '" + timestamp_message + "' " + whole_file_path
    #execute our command
    call([timestamp_command], shell= True)
    print("We have timestamped our picture!")
    
    #Advance our picture counter
    picture_counter += 1
    
    sleep(2)




#Take a picture
"""
with picamera.PiCamera() as camera:
    camera.resolution = (1280,720)
    camera.capture(file_name)
    print("We have taken a picture")
"""

#our timestamp's message
"""
print("About time timestamp our picture")
timestamp_message = "Check out this message!"
#Specify the command we want to call
#usr/bin/convert /home/pi/Desktop/Python_PROJECTS/Pi_Camera/TUTORIAL/Take_Picture/CAPTURES/img.jpg -pointsize 32 -fill red -annotate +700+500 'dzien dobry' /home/pi/Desktop/Python_PROJECTS/Pi_Camera/TUTORIAL/Take_Picture/CAPTURES/new_img.jpg
timestamp_command = "/usr/bin/convert "+ file_name + " -pointsize 32 -fill red -annotate +700+500 '" + timestamp_message + "' " + file_name
#execute our command
call([timestamp_command], shell= True)
print("Picture has been timestamped")
"""