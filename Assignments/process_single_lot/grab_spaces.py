import numpy as np
import cv2 as cv
from scipy.spatial import distance

from matplotlib import pyplot as plt
from json import dumps,loads
import pprint as pp
from sys import argv, exit


def load_spaces(definition_file):
    f = open(definition_file,'r')
    spaces = loads(f.read())

    return spaces

def extract_points(space):
    points = []
    for i in range(4):
        x = int(space['contour']['point'][i]['x'])
        y = int(space['contour']['point'][i]['y'])
        points.append((x,y))
    return points

def draw_parking_space(points,img):
    colors = [(0,0,255),(0,255,0),(255,0,0),(255,255,0)]
    for i in range(4):
        x1 = points[i][0]
        y1 = points[i][1]
        x2 = points[(i+1)%4][0]
        y2 = points[(i+1)%4][1]
        cv.line(img, (x1,y1),(x2,y2),colors[i], 2)

def make_parallelogram(p,type=0):
    """
    Types: 0 = smallest area , 1 = largest area , 2 = avg area
    """
    for i in range(4):
        a = p[i]
        b = p[(i+1) % 4]
        dst = distance.euclidean(a,b)
        print(dst)
    print()

def new_space_image(pixels,width,height):
    blank_image = np.zeros((height,width,3), np.uint8)


if __name__=='__main__':

    if len(argv) < 3:
        exit()
    
    definition_file = argv[1]
    image_file = argv[2]
    

#    arg1='pklot-json.json'
#    arg2='2012-12-16_12_05_07.jpg'
#    
#    definition_file = arg1
#    image_file = arg2

    spaces = load_spaces(definition_file)
    
    img = cv.imread(image_file)
    for space in spaces:
        points = extract_points(space)
        make_parallelogram(points)
        
        draw_parking_space(points,img)
    # Typical opencv methods to show images
    cv.imshow('Draw01',img)
    each_space=0
    for space in spaces:
        x=int(space['contour']['point'][1]['x'])
        y=int(space['contour']['point'][1]['y'])
        h=int(space['rotatedRect']['size']['h'])
        w=int(space['rotatedRect']['size']['w'])
        w=int(w/2)
        # NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]
        crop_img=img[y:y+h, x:x+w]
        cv.imwrite("spaces/"+ str(each_space) +".png", crop_img)
        hist = cv.calcHist([crop_img], [0, 1], None, [180, 256], [0, 180, 0, 256])
        np.savetxt('histograms/'+str(each_space)+".csv", hist, delimiter=',')
        each_space=each_space+1
    cv.waitKey(0)
    # plt.imshow(img)
    # plt.show()