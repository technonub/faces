#!/usr/bin/env python3
import sys
import cv2
from PIL import Image

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# open hat img
hat = Image.open('hat.png')
o_w, o_h = hat.size

def add_hats(filename):
    # open img with opencv
    cv2_img = cv2.imread(filename)
    # convert img to pillow format
    pil_img = Image.fromarray(cv2.cvtColor(cv2_img,cv2.COLOR_BGR2RGB))

    # find faces with opencv
    gray = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces :
        # attept to put hat
        # resize hat
        h_w = int(round(1.4 * w))
        h_h = int(round((o_h * h_w) / o_w))
        h_x = int(round(x - 0.2 * w))
        h_y = int(round(y - (h_h - 0.2 * h)))
        resized_hat = hat.resize((h_w, h_h))
        pil_img.paste(resized_hat, (h_x,h_y), mask=resized_hat)

    # TODO: save image
    return pil_img

if __name__ == "__main__":
    # open images
      for arg in sys.argv[1:]:
        img = add_hats(arg)
        img.show()
        img.save("img.jpg")
