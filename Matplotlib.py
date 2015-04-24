import cv2
import sys
from matplotlib import pyplot as plt
img_name = sys.argv[1]
img = cv2.imread(img_name,0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()