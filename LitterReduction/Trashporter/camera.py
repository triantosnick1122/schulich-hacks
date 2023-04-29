import cv2
import threading

class VideoCamera(object):
    def __init__(self):
        camera_feed_val = 0
        while camera_feed_val < 5:
            try:
                self.video = cv2.VideoCapture(camera_feed_val)
                (self.grabbed, self.frame) = self.video.read()
                _, jpeg = cv2.imencode('.jpg', self.frame)
                break
            except:
                camera_feed_val += 1
        if camera_feed_val >= 5:
            raise Exception("Failed to identify working camera.")
        else:
            threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
    
    def get_image(self):
        image = self.frame
        return image

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
