import picamera

camera = picamera.PiCamera()


def take_picture(file="cameraOutput.png"):
    """Take a picture and save to disk

        Notes: Default file is 'cameraOutput.png'
        Params:
            file = location to save the image
        Returns:
            Bool if picture was captured
    """
    try:
        camera.start_preview()
        camera.capture(file, format='png')
        camera.stop_preview()
        return True
    except:
        return False
