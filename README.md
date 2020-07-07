# Edit_Blue_Background
Using Computer Vision technique, we edit blue background of an image.

First we detect the blue screen and created a mask.
Then using mask, we remove the blue background from our image and the took the new background image.
From the background image, we remove the area where we will put our object later on using mask only.

Then we join the two image to a comple one.
