!pip install picamera
import picamera

if __name__ == '__main__':
    camera = picamera.PiCamera()

    camera.start_preview()
    camera.capture('cameraOutput.png', format='png')
    camera.stop_preview()
