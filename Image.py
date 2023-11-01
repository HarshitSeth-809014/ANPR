import os
import cv2
import datetime


def get_data():
    date = str(datetime.date.today())
    time = datetime.datetime.now().strftime("%H_%M_%S")
    return date+" "+time

cam_port = 0
directory = '.\Images'


def take_photo():
    cam = cv2.VideoCapture(cam_port)
    
    result, image = cam.read()
    data = get_data()
    filename = "img{}.png".format(data)
    if result:
        os.chdir(directory)
        cv2.imwrite(filename, image)
        os.chdir('..')
        return [filename, data]
    else:
        return None
