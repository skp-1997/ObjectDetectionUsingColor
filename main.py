# Import libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt


# Define colour code
color_dict_HSV = {'black': [[180, 255, 30], [0, 0, 0]],
              'white': [[180, 18, 255], [0, 0, 231]],
              'red1': [[180, 255, 255], [159, 50, 70]],
              'red2': [[9, 255, 255], [0, 50, 70]],
              'green': [[89, 255, 255], [36, 50, 70]],
              'blue': [[128, 255, 255], [90, 50, 70]],
              'yellow': [[35, 255, 255], [25, 50, 70]],
              'purple': [[158, 255, 255], [129, 50, 70]],
              'orange': [[24, 255, 255], [10, 50, 70]],
              'gray': [[180, 18, 230], [0, 0, 40]]}

# Read the image
bgr = cv2.imread('input/index4.jpeg')

# Convert it to HSV
hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)

# Set the range for a color
lower = np.array(color_dict_HSV['red1'][1])
upper = np.array(color_dict_HSV['red1'][0])

# Threshold the HSV to get particular colour only
mask = cv2.inRange(hsv, lower, upper)

# Bitwise AND mask on original image
thresh_frame = cv2.bitwise_and(bgr, bgr, mask=mask)

# Converting to gray scale to apply findContours function
thresh_frame_gray = cv2.cvtColor(thresh_frame, cv2.COLOR_BGR2GRAY)

# Find max contour on masked image
# Finding contour of moving object
cnts,_ = cv2.findContours(thresh_frame_gray.copy(),
                    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)

for contour in cnts:
    if cv2.contourArea(contour) > 50:  # Set the pixels size threshold here
        (x, y, w, h) = cv2.boundingRect(contour)
        # making green rectangle around the moving object
        cv2.rectangle(rgb, (x, y), (x + w, y + h), (255, 0, 0), 3)

# Plotting the results
f, axarr = plt.subplots(2,3)

axarr[0,0].imshow(bgr)
axarr[0,0].set_title('Original Image_in_RGB')
axarr[0,1].imshow(hsv)
axarr[0,1].set_title('HSV')
axarr[0,2].imshow(mask)
axarr[0,2].set_title('Mask_Color')
axarr[1,0].imshow(thresh_frame)
axarr[1,0].set_title('Bitwise_Threshold_Image')
axarr[1,1].imshow(thresh_frame_gray)
axarr[1,1].set_title('Threshold_Image_Gray')
axarr[1,2].imshow(rgb)
axarr[1,2].set_title('Final_Output')


# plt.imshow(rgb)
plt.show()
# cv2.imwrite('output_index1.jpeg',bgr)







'''
########### How to find HSV value for color #############
green = np.uint8([[[0,255,0 ]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)

print( hsv_green )
[[[ 60 255 255]]]

lower : [H-10, 100, 100]
upper : [H+10, 255, 255]
'''