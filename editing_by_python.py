# installation of pillow library 
# change the image extension 
# resize the image file
# resize the multiple images using the loop
# sharpness 
# brightness
# color
# constrast
# image blur,gaussianblur

# we need a pillow library for editing the image
# to install that open the terminal and type the 'pip install pillow'
# write capital P in pillow
# ther is a image class in image module 
# first we have to open it no need write the full path,bcz working in the same directory 
# we can convert the image in any form like the png,pdf ect..
# if u dont wanna save the image ,just check how it would be after editing..use the show command

from PIL import Image,ImageEnhance,ImageFilter
import os
img1 = Image.open('mobile_bill.pdf.docx')
img1.save('bill.pdf')
img1.save('charizard.pdf')
img1.show()
# reszie the image 
# first make the tuple () write the radius in it and store that in a variable
# use the thumbnail command to do it 
# for resize the mutiple images use the loop
# for this u have to import the os module
# for working with sharpness,color etc..we have to import the module 'imageenhance'
# first make the object and store it in a variable
# sharpness----class
# values : 0--blur image, 1--original pic,2--increase sharpness,3--more,4--more
# color ----class
# values : 0--black and white ,1--original pic,2--increse,3--more
# brigtness --class
# values : 
# constrast -- class 
# 
# for bluring the image we have to import the  Imagefilter
# 


max_size = (250,250)
img1.thumbnail(max_size)
img1.save('charizard.png')
for item in os.listdir():
    if item.endswith('p'):
        img1 =  Image.open(item)
        filename,extension = os.path.splitext(item)
        img1.save(f'{filename}.png')

enhancer = ImageEnhance.Sharpness(img1)              
enhancer.enhance(5).save('long.jpg')                
enhancer = ImageEnhance.Color(img1)                  
enhancer.enhance(0).save('edited.jpg')              
enhancer = ImageEnhance.Brightness(img1)            
enhancer = ImageEnhance.Contrast(img1)
enhancer.enhance(5).save('edited.jpg')

img1.filter(ImageFilter.GaussianBlur()).save('editing2.png') 

os.remove('long.jpg')
os.remove('editing2.png')
os.remove('charizard.png')
os.remove('edited.jpg')