import time
import easygopigo3 as easy
import random


def move():
    gpg = easy.EasyGoPiGo3()
    walld_distance_sensor = gpg.init_distance_sensor()
    
    if random.randint(0,1) == 0: 
        gpg.right()
    else:
        gpg.left()
    time.sleep(1)
    gpg.forward()
    
    while True:
        print("Distance Sensor Reading (mm): " + str(walld_distance_sensor.read_mm()))
    
        if walld_distance_sensor.read_mm() <= 50:
            print("Stopping, Collision Detected")
            gpg.stop()
            break
