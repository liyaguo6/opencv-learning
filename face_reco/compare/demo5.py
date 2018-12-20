# # 识别图片中的人脸
# import face_recognition
# li_image = face_recognition.load_image_file("li.jpg")
# gong_image = face_recognition.load_image_file("gong.jpg")
# unknown_image = face_recognition.load_image_file("li_test.jpg")
#
# li_encoding = face_recognition.face_encodings(li_image)[0]
# gong_encoding = face_recognition.face_encodings(gong_image)[0]
# unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
#
# results = face_recognition.compare_faces([li_encoding, gong_encoding], unknown_encoding )
# labels = ['li', 'gong']
#
# print('results:'+str(results))
# #
# for i in range(0, len(results)):
#     if results[i] == True:
#         print('The person is:'+labels[i])



#########################case2#################
import face_recognition
import cv2
import os
video_capture = cv2.VideoCapture(0)
path="./images/"
total_images=[]
total_image_name=[]
total_face_encoding=[]
for fn in os.listdir(path):
    total_face_encoding.append(face_recognition.face_encodings(face_recognition.load_image_file(path+fn))[0])
    fn=fn[:(len(fn)-4)]
    total_image_name.append(fn)

while True:
    # 抓取一帧视频q
    ret,frame = video_capture.read()
    #发现在视频帧所有的脸和face_enqcodings
    face_locations = face_recognition.face_locations(frame)
    face_encodings= face_recognition.face_encodings(frame,face_locations)
    #在这个视频中循环遍历每个人人脸
    for (top,right,bottom,left),face_encoding in zip(face_locations,face_encodings):
        for i,v in enumerate(total_face_encoding):
            match = face_recognition.compare_faces([v],face_encoding,tolerance=0.5)
            name = 'Unknown'
            if match[0]:
                name = total_image_name[i]
                break
        # 画出一个框，框住人脸
        cv2.rectangle(frame,(left,top),(right,bottom),(0,0,255))
        #画出一个带名字的标签，放在框下
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame,name,(left+6,bottom-6),font,2.0,(255,255,255),1)

    cv2.imshow('Video',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()




