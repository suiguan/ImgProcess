#This script used to crop image vertically

import cv2
import sys

if len(sys.argv) != 4:
   print("usage: python %s <img> <cut ratio begin> <cut ratio end>") 
   sys.exit(-1)

img = sys.argv[1]
if img.find(".") < 0: raise Exception("invalid filename %s" % img)
ext = img[img.find("."):]
cutBeg = float(sys.argv[2])
cutEnd = float(sys.argv[3])

if cutBeg < 0 or cutBeg >= 1: raise Exception("Invalid cutBeg %s" % cutBeg)
if cutEnd <= 0 or cutEnd > 1: raise Exception("Invalid cutEnd %s" % cutEnd)
if cutBeg >= cutEnd: raise Exception("Invalid %s, %s" % (cutBeg, cutEnd))

arr = cv2.imread(img)
h, w, c = arr.shape
if cutEnd == 1: arr = arr[0:int(cutBeg*h),:,:]
elif cutBeg == 0: arr = arr[int(cutEnd*h):,:,:]
else: raise Exception("not support range %s %s" % (cutBeg, cutEnd))


cv2.imshow("out", cv2.resize(arr, (300,300)))
if cv2.waitKey(-1) == ord('s'): cv2.imwrite("_img_out%s" % ext, arr)
