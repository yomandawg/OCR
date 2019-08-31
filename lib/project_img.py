#!/usr/bin/etc python
import cv2
import numpy as np
import pytesseract
from PIL import Image
# from imutils.perspective import four_point_transform
# from imutils import contours
# import imutils
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


number_of_img = 3
class Recognition:
     def ExtractNumber(self, input_image):
          imag2 = cv2.imread(input_image)
          # print(image)
          # img=cv2.imread(Number,cv2.IMREAD_COLOR)
          plt.figure(figsize=(40, 40))
          plt.subplot(number_of_img,1,1)
          plt.imshow(imag2,cmap='gray')
          # plt.imshow(imag2)

          gray = cv2.cvtColor(imag2, cv2.COLOR_BGR2GRAY)
          plt.subplot(number_of_img,1,2)
          plt.imshow(gray,cmap='gray')
          # plt.imshow(gray)

          blurred = cv2.GaussianBlur(gray, (5, 5), 0)
          plt.subplot(number_of_img,1,3)
          plt.imshow(blurred,cmap='gray')
          # plt.imshow(blurred)

          plt.show()


          # edged = cv2.Canny(blurred, 0, 10 , 200)
          # plt.subplot(number_of_img,1,4)
          # # plt.imshow(edged,cmap='gray')
          # plt.imshow(edged)
          #
          # blurred_2 = cv2.GaussianBlur(edged, (7, 7), 0)
          # plt.subplot(number_of_img,1,5)
          # # plt.imshow(blurred_2,cmap='gray')
          # plt.imshow(blurred_2)
          #
          # edged_2 = cv2.Canny(blurred_2, 0, 10 ,200)
          # plt.subplot(number_of_img,1,6)
          # # plt.imshow(edged_2,cmap='gray')
          # plt.imshow(edged_2)


          # plt.show()

          # ret, img_th = cv2.threshold(edged, 10, 200, cv2.THRESH_BINARY_INV)
          # contours, hierachy = cv2.findContours(img_th.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
          # rects = [cv2.boundingRect(each) for each in contours]
          # tmp = [w * h for (x, y, w, h) in rects]
          # tmp.sort()
          # print(len(rects))
          # rects = [(x, y, w, h) for (x, y, w, h) in rects if ((w * h > 100) and (w * h < 2000))]
          # print(rects)
          # for rect in rects:
          #      # Draw the rectangles
          #      cv2.rectangle(imag2, (rect[0], rect[1]),
          #                    (rect[0] + rect[2], rect[1] + rect[3]), (0, 200, 0), 5)

          # plt.figure(figsize=(15, 12))
          # plt.imshow(imag2)
          # plt.show()
          # print(rects)
          

Recognition().ExtractNumber('3.jpg')
    
          

