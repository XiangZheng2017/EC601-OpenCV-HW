# EC601-OpenCV-HW
Boston University College of Engineering - EC601 HW3 - OpenCV Exercises

## Exercise 1

**1. How does a program read the cvMat object, in particular, what is the order of the pixel structure?**

The cvMat is a way to represent the pixels in an image in a matrix form. Therefore, pixel values of a cvMat file can be accessed by using the cvMatName.at<datatype>(x,y) where we can access a particular pixel at matrix entry point (x,y) where (0,0) would be the top-left entry of the matrix. Additionally, if the pixel has multiple color channels, then we could access a particular color channel by invoking cvMatName.at<datatype>{x,y)[index] where index allows us to access particular values of the color channels (i.e. RGB). This method requires that we know the datatype of the entries.
  
## Exercise 2
  
  **1. ColorImage.cpp is a program that takes a look at colorspace conversions in OpenCV. Run the code in ColorImage.cpp and comment on the outputs. Implement the same thing in Python and save each image.**

The outputs of this file are the Lena.png image, broken up into several different colorspaces. We are shown the red, green, and blue intensities of the image. Additionally, we can see the Y, Cr, Cb, Hue, Saturation and value colorspaces.

**2. Print out the values of the pixel at (20,25) in the RGB, YCbCr and HSV versions of the image. What are the ranges of pixel values in each channel of each of the above mentioned colorspaces?**

- RGB(20,25) = 106,122,225
- HSV(20,25) = 4,135,225
- YCC(20,25) = 151,181,103

These values range from 0-225. 


Appropriate code and output for this exercise can be found in the Exercise 2 folder.

## Exercise 4

**1. Look at Threshold.cpp and implement the code in Python, and observe the results for different threshold values. Comment on the results.**

The output of this program shows the same image with different thresholds applied to its grayscaled version. We can see that different thresholds highlight/decimate certain features of the image (ex: thresholded image keeps the face relatively intact but the nose features are completely gone). We also see that Adaptive filtering keeps a lot of the same features of the original image.

**2. What are the disadvantages of binary threshold?**

Binary threshold was designed to highlight one area while completely decimating the other (ex: highlighting foreground vs background of an image). While this can be useful in some applications, we can see a lot of loss of details that we may want to keep.

**3. When is Adaptive Threshold useful?**

Adaptive thresholding allows us to apply multiple thresholds at the same time. This can be useful when we want to perform multiple processes on the same image at different levels. A perfect example would be when you compare our adaptive threshold image to out binary threshold image. While the binary imagine completely gets rid of certain features, the adaptive threshold (which applies a binary threshold as one of its components) allows us to perform a similar masking but keep certain features of the image.

Appropriate code and outputs can be found in folder Exercise 4
