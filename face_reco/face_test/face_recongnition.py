import face_recognition
import cv2
import os
import time
from build_datafile import get_data
import threading


class FaceRecon():
    def __init__(self,path):
        self.name ='Unknow'
        self.data = get_data(path)
        self.video = cv2.VideoCapture(0)
        self.frame =None
    def capture_image(self):
        # 抓取一帧视频q
        ret, self.frame = self.video.read()
        self.face_locations = face_recognition.face_locations(self.frame)
        self.face_encodings = face_recognition.face_encodings(self.frame, self.face_locations)
        # 在这个视频中循环遍历每个人人脸

    def recongnition(self):
        for (top, right, bottom, left), face_encoding in zip(self.face_locations, self.face_encodings):
            print("1：", time.time())
            for i, v in enumerate(self.data.values()):
                match = face_recognition.compare_faces([v], face_encoding, tolerance=0.5)
                if match[0]:
                    self.name = list(self.data.keys())[i]
                    print("2：", time.time())
                    break
                else:
                    self.name='Unknow'
            cv2.rectangle(self.frame, (left, top), (right, bottom), (0, 0, 255))
            # 画出一个带名字的标签，放在框下
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(self.frame, self.name, (left + 6, bottom - 6), font, 2.0, (255, 255, 255), 1)

    def close(self):
            self.video.release()
            cv2.destroyAllWindows()

    def imag_show(self):
        while True:
            self.capture_image()
            self.recongnition()
            cv2.imshow('Video', self.frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.close()
                break


if __name__ == '__main__':
    fr = FaceRecon('./ImageSource.pk')
    t = threading.Thread(target=fr.imag_show)
    t.start()
    while 1:
        time.sleep(3)
        print(fr.name)