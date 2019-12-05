import picamera

def take_picture(file="cameraOutput.png"):
    """Take a picture and save to disk

        Notes: Default file is 'cameraOutput.png'
        Params:
            file = location to save the image
    """
    camera = picamera.PiCamera()
    camera.start_preview()
    camera.capture(file, format='png')
    camera.stop_preview()
