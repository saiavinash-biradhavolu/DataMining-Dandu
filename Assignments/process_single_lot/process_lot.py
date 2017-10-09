#Team Members: 
#Muni Bhupathi Reddy Dandu
#Karan Madishetty
#Sai Avinash Reddy Biradhavolu

from lot_xml_to_json import xmltojson
import numpy as np
import cv2 as cv
import sys
import os
import subprocess

img = cv.imread('2012-12-16_12_05_07.jpg')
filename='2012-12-16_12_05_07.xml'
#img = cv.rectangle(img, (250,70), (330,150), (0,255,0), 4)
#crop_img = img[0:100, 0:100]
#font = cv.FONT_HERSHEY_SIMPLEX
#cv.putText(img, "This one!", (230, 50), font, 0.8, (0, 255, 0), 2, cv.LINE_AA)
cv.imshow('Draw01',img)
#cv.imshow("cropped", crop_img)

xmltojson(filename,'pklot-json.json',)
arg0="grab_spaces.py"
arg1='pklot-json.json'
arg2='2012-12-16_12_05_07.jpg'

subprocess.call(["python",arg0,arg1,arg2], shell=False)
cv.waitKey(0)