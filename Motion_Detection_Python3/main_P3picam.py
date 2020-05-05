import P3picam_Python3
import picamera


motion_state = False
motion_counter = 0;

while True:
    motion_state = P3picam_Python3.motion()
    #print(motion_state)
    if motion_state == True:
        print("Motion detected")
        with picamera.PiCamera() as camera:
            motion_file_path = "./CAPTURED/motion"+str(motion_counter)+".jpg"
            camera.resolution = (1280,720)
            camera.capture(motion_file_path)
            motion_counter += 1
            
 