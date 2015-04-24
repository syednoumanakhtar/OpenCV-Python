import cv2
import sys

img_name = sys.argv[1]
im = cv2.imread(img_name)
gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
thresh = cv2.adaptiveThreshold(blur,255,1,1,11,2)

cv2.imshow('OriginalImage',im)
k = cv2.waitKey(0)
cv2.imshow('GrayScaleImage',gray)
k = cv2.waitKey(0)
cv2.imshow('BlurredImage',blur)
k = cv2.waitKey(0)
cv2.imshow('ThresholdingImage',thresh)
k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()