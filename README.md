# EC601-OpenCV-HW
Boston University College of Engineering - EC601 HW3 - OpenCV Exercises

##Exercise 1

**1. How does a program read the cvMat object, in particular, what is the order of the pixel structure?**

The cvMat is a way to represent the pixels in an image in a matrix form. Therefore, pixel values of a cvMat file can be accessed by using the cvMatName.at<datatype>(x,y) where we can access a particular pixel at matrix entry point (x,y) where (0,0) would be the top-left entry of the matrix. Additionally, if the pixel has multiple color channels, then we could access a particular color channel by invoking cvMatName.at<datatype>{x,y)[index] where index allows us to access particular values of the color channels (i.e. RGB). This method requires that we know the datatype of the entries.
  
  ##Exercise 2
  
  **1. ColorImage.cpp is a program that takes a look at colorspace conversions in OpenCV. Run the code in ColorImage.cpp and comment on the outputs. Implement the same thing in Python and save each image.**

The outputs of this file are the Lena.png image, broken up into several different colorspaces. We are shown the red, green, and blue intensities of the image. Additionally, we can see the Y, Cr, Cb, Hue, Saturation and value colorspaces.

**2. Print out the values of the pixel at (20,25) in the RGB, YCbCr and HSV versions of the image. What are the ranges of pixel values in each channel of each of the above mentioned colorspaces?**

Appropriate code and output for this exercise can be found in the Exercise 2 folder.
