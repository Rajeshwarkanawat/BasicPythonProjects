import cv2

#Configuration Prameters
source = "img.jpeg"
destination = "newImg.jpeg"
scale_Percent = 50

src = cv2.imread(source,cv2.IMREAD_UNCHANGED)

# cv2.imshow("Title",src) Used to show the image 
# cv2.waitKey(0) Used to hold the image 

#Percent by which the image is resized 

#Calculate the 50 percent of orginal dimension
new_width = int(src.shape[1] * scale_Percent / 100)
new_height = int(src.shape[0] * scale_Percent / 100)

#Resize image
output = cv2.resize(src,(new_width,new_height))

cv2.imwrite(destination,output)
cv2.waitKey(0   )
