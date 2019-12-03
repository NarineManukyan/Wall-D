import time
import easygopigo3 as easy

gpg = easy.EasyGoPiGo3()
walld_distance_sensor = gpg.init_distance_sensor()

gpg.forward()
while True:
    print("Distance Sensor Reading (mm): " + str(walld_distance_sensor.read_mm()))

    if walld_distance_sensor.read_mm() <= 50:
        print("Stopping, Collision Detected")
        gpg.stop()
        # break
    time.sleep(1)
    gpg.right()
    time.sleep(1)
    gpg.forward()
