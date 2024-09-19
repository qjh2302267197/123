import cv2
import  numpy as np

HB = np.zeros((640,640,3),np.uint8)
cv2.imshow("HB",HB)
cv2.waitKey()