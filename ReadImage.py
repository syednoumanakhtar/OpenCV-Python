import cv2
import sys

img_name = sys.argv[1]
im = cv2.imread(img_name)

cv2.imshow('OriginalImage',im)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()