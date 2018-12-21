import cv2
import face_recognition
import os
import pickle
import shutil


def getImage(src_path,tem_path):
    for fn in os.listdir(tem_path):
        filepath=os.path.join(tem_path,fn)
        total_face_encoding=face_recognition.face_encodings(face_recognition.load_image_file(filepath))[0]
        shutil.move(filepath,src_path)
        fn = fn[:(len(fn) - 4)]
        total_image_name = fn
        yield {total_image_name:total_face_encoding}

# data = {}

def saveImage(ImagePath,**kwargs):
    if os.listdir(kwargs['tem_path']):
        with open(ImagePath, 'rb+') as fp:
            data=pickle.load(fp)
        with open(ImagePath,'wb+') as fp:
            new_data={}
            for i in getImage(kwargs['src_path'],kwargs['tem_path']):
                new_data.update(i)
            new_data.update(data)
            pickle.dump(new_data,fp)
            # return data


def get_data(ImagePath):
    with open(ImagePath, 'rb+') as fp:
        data = pickle.load(fp)
        return data



if __name__ == '__main__':

    # saveImage('./ImageSource.pk',src_path='./raw_images/',tem_path='./temp_images/')
    ret=get_data('./ImageSource.pk')
    print(ret)
