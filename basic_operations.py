import cv2
import numpy as np

input = cv2.imread('images/Modi.jpg')
cv2.imshow('Test Image', input)
cv2.imwrite('output.jpg', input)

print('Height of Image:', int(input.shape[0]), 'pixels')
print('Width of Image: ', int(input.shape[1]), 'pixels')

cv2.waitKey() 
cv2.destroyAllWindows() 