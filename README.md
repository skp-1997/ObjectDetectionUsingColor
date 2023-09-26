# Object Detection using Color

This project detects the object using its color 

# Outputs

![output_index1](https://github.com/skp-1997/ObjectDetectionUsingColor/assets/97504177/c066586c-efcb-43b9-b2ae-1d106b049eed)
![output_images](https://github.com/skp-1997/ObjectDetectionUsingColor/assets/97504177/168f1aae-b538-4ad8-804f-7204a2cf4a4e)


# Procedure :

1. Read the image using opencv
2. Convert to HSV format
3. Generate Mask using lower and upper threshold of targeted Color
3. Apply the Mask on Original Image so only particular color is visible
4. Convert to graysacle before apply findContour as it works only with grayscale images
5. Finally use contourArea to filter contours with required pixels size and draw bounding box


# Things to remember :

1. Opencv works on BGR image format and Matplotlib works on RGB format
2. Set the contourArea threshold value as per object you are detecting
3. You can change the color of object by generating accordingly mask
4. You can get the upper and lower threshold to generate particular color mask from dictionary in the code
