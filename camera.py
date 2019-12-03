import picamera

def take_picture(file="cameraOutput.png"):
    camera = picamera.PiCamera()
    camera.start_preview()
    camera.capture(file, format='png')
    camera.stop_preview()
