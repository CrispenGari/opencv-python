
import cv2
import numpy as np
cap = cv2.VideoCapture('solidWhiteRight.mp4')
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 200)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 250)

while cap.isOpened():
    _, image= cap.read()
    #print(image.shape)
    height=image.shape[0]
    width=image.shape[1]
    def draw_the_line(img,lines):
        img=np.copy(img)
        blank_image=np.zeros((img.shape[0],img.shape[1],3),dtype=np.uint8)

        for line in lines:
            for x1,y1,x2,y2 in line:
                cv2.line(blank_image,(x1,y1),(x2,y2),(0,255,0),thickness=10)
        img=cv2.addWeighted(img,0.8,blank_image,1,0.0)
        return img


    def region_of_interst(img,vertices):
        mask=np.zeros_like(img)
        #channel_count=img.shape[2]
        match_mask_color=255
        cv2.fillPoly(mask,vertices,match_mask_color)
        mask_image=cv2.bitwise_and(img,mask)
        return mask_image


    region_of_interst_vertices=[(0,height),(width/2,height/2),(width,height)]
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    canny=cv2.Canny(gray,100,200)

    cropped=region_of_interst(canny,np.array([region_of_interst_vertices],np.int32))
    line1=cv2.HoughLinesP(cropped,rho=6,theta=np.pi/60,threshold=160,lines=np.array([]),minLineLength=40,maxLineGap=20)

    image_width_line=draw_the_line(image, line1)
    cv2.imshow("Lanes", image_width_line)
    if cv2.waitKey(10) & 0xFF == 27:
        break
