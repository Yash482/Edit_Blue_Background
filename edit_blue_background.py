import numpy as np
import cv2 #computer_vision library
import matplotlib.pyplot as plt

#read image with blue screen
img = cv2.imread("pizza.jpeg")
#always make copy to edit
img_copy = np.copy(img)
#By default, openCV takes img as BGR color code insted of RGB
#So we convert back to use properly
img_copy = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#note the img details as it will be required to resize the new background
#Background needs to be of same size
#print(img_copy.shape)

"""
Now, 
1st we define a certain range of blue which we want to detect
"""
lower_blue = np.array([0, 0, 225])    #lower range value
upper_blue = np.array([40, 40, 255])  #upper range value

#now we create a mask which is an image only, it has white on portion which falls in the given range
#and the part get black
#it means background part will get white and pizza will get black
mask = cv2.inRange(img_copy, lower_blue, upper_blue)
#plt.imshow(mask)

#now we remove the blue background by using mask !=0 i.e.. white
masked_img = np.copy(img_copy)   #1st make copy
masked_img[mask != 0] = [0,0,0]  #make backgroung black
#plt.imshow(masked_img)
#we get pizza with black backgroung

#read desired backgroung img and cnvrt the color and resize it using the image details
background_img = cv2.imread("bck_ground.jpg")
background_img = cv2.cvtColor(background_img, cv2.COLOR_BGR2RGB)
crop_background = background_img[0:414, 0:650]

#here we remove the pizza part and leave the rest
crop_background[mask ==0] = [0,0,0]

#we did this so that now we can add simply to get complete img
complete_img = masked_img + crop_background
plt.imshow(complete_img)

#done