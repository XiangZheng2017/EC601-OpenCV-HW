# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 22:49:55 2017

@author: Frank Tranghese
Boston University College of Engineering
EC601 - Product Design
OpenCV HW - Exercise 1
"""
import cv2

lena = cv2.imread('Test_images/Lenna.png') #load Lenna image

[b,g,r] = cv2.split(lena) #split into color channels

cv2.imshow('Blue',b)
cv2.imwrite('Blue.png',b)
cv2.imshow('Red',r) 
cv2.imwrite('Red.png',r)
cv2.imshow('Green',g)
cv2.imwrite('Green.png',g)

hsv_lena = cv2.cvtColor(lena, cv2.COLOR_BGR2HSV) #convert to HSV

[h,s,v] = cv2.split(hsv_lena) #split into HSV channells

cv2.imshow('Hue',h)
cv2.imwrite('Hue.png',h)
cv2.imshow('Saturation',s)
cv2.imwrite('Saturation.png',s)
cv2.imshow('Value',v)
cv2.imwrite('Value.png',v)

YCC_lena = cv2.cvtColor(lena, cv2.COLOR_BGR2YCR_CB) #convert to YCrCb

[y,Cb,Cr] = cv2.split(YCC_lena) #split YCrCb channels

cv2.imshow('Y',y)
cv2.imwrite('Y.png',y)
cv2.imshow('Cb',Cb)
cv2.imwrite('Cb.png',Cb)
cv2.imshow('Cr',Cr)
cv2.imwrite('Cr.png',Cr)

cv2.waitKey(0)