import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import CoDrone

drone = CoDrone.CoDrone()
drone.pair(drone.Nearest)
drone.takeoff()

lowerBound=np.array([0,120,70])
upperBound=np.array([10,255,255])

lower = np.array([170,120,70])
upper = np.array([180,255,255])

cam= cv2.VideoCapture(0)
kernelOpen=np.ones((5,5))
kernelClose=np.ones((20,20))

while True:
    ret, img = cam.read()
    img = cv2.resize(img,(1113,720))

    #QR code reader
    decodedImage = pyzbar.decode(img)
    for obj in decodedImage:
        print(obj.data)

    #convert BGR to HSV
    imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    # create the Mask
    mask=cv2.inRange(imgHSV,lowerBound,upperBound)
    mask2 = cv2.inRange(imgHSV,lower,upper)
    mask = mask + mask2
    #morphology
    maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
    maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)

    maskFinal=maskClose
    conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    cv2.drawContours(img,conts,-1,(255,0,0),3)
    for i in range(len(conts)):
        x,y,w,h=cv2.boundingRect(conts[i])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255), 2)

    #drawing reference rectangle (where object must be)
    height = img.shape[0]
    width = img.shape[1]
    
    startrow, startcol = int(height/2)-300, int(width/2)-300
    endrow, endcol = int(height/2)-100, int(width/2)-100
    cropped = maskClose[startrow:endrow, startcol:endcol]
    cv2.rectangle(img, (int(width/2)-300,int(height/2)-300), (int(width/2)-100,int(height/2)-100), (255,0,0), 4)

    croppedsize = np.size(cropped)
    nonzero = np.count_nonzero(cropped)
    percent = 100*nonzero/croppedsize
    csum = percent
    #print(round(percent), end = " ")

    great = percent
    index = 1

    startrow, startcol = int(height/2)-300, int(width/2)-100
    endrow, endcol = int(height/2)-100, int(width/2)+100
    cropped2 = maskClose[startrow:endrow, startcol:endcol]
    cv2.rectangle(img, (int(width/2)-100,int(height/2)-300), (int(width/2)+100,int(height/2)-100), (255,0,0), 4)

    croppedsize = np.size(cropped2)
    nonzero = np.count_nonzero(cropped2)
    percent = 100*nonzero/croppedsize
    csum = csum + percent
    #print(round(percent), end = " ")

    if percent >= great:
        great = percent
        index = 2
    
    startrow, startcol = int(height/2)-300, int(width/2)+100
    endrow, endcol = int(height/2)-100, int(width/2)+300
    cropped3 = maskClose[startrow:endrow, startcol:endcol]
    cv2.rectangle(img, (int(width/2)+100,int(height/2)-300), (int(width/2)+300,int(height/2)-100), (255,0,0), 4)

    croppedsize = np.size(cropped3)
    nonzero = np.count_nonzero(cropped3)
    percent = 100*nonzero/croppedsize
    csum = csum + percent
    #print(round(percent), end = " ")

    if percent > great:
        great = percent
        index = 3

    startrow, startcol = int(height/2)-100, int(width/2)-300
    endrow, endcol = int(height/2)+100, int(width/2)-100
    cropped4 = maskClose[startrow:endrow, startcol:endcol]
    cv2.rectangle(img, (int(width/2)-300,int(height/2)-100), (int(width/2)-100,int(height/2)+100), (255,0,0), 4)

    croppedsize = np.size(cropped4)
    nonzero = np.count_nonzero(cropped4)
    percent = 100*nonzero/croppedsize
    csum = csum + percent
    #print(round(percent), end = " ")

    if percent > great:
        great = percent
        index = 4

    startrow, startcol = int(height/2)-100, int(width/2)-100
    endrow, endcol = int(height/2)+100, int(width/2)+100
    cropped5 = maskClose[startrow:endrow, startcol:endcol]
    cv2.rectangle(img, (int(width/2)-100,int(height/2)-100), (int(width/2)+100,int(height/2)+100), (255,0,0), 4)

    croppedsize = np.size(cropped5)
    nonzero = np.count_nonzero(cropped5)
    percent = 100*nonzero/croppedsize
    csum = csum + percent
    #print(round(percent), end = " ")

    if percent >= great:
        great = percent
        index = 5

    startrow, startcol = int(height/2)-100, int(width/2)+100
    endrow, endcol = int(height/2)+100, int(width/2)+300
    cropped6 = maskClose[startrow:endrow, startcol:endcol]
    cv2.rectangle(img, (int(width/2)+100,int(height/2)-100), (int(width/2)+300,int(height/2)+100), (255,0,0), 4)

    croppedsize = np.size(cropped6)
    nonzero = np.count_nonzero(cropped6)
    percent = 100*nonzero/croppedsize
    csum = csum + percent
    #print(round(percent), end = " ")

    if percent > great:
        great = percent
        index = 6

    startrow, startcol = int(height/2)+100, int(width/2)-300
    endrow, endcol = int(height/2)+300, int(width/2)-100
    cropped7 = maskClose[startrow:endrow, startcol:endcol]
    cv2.rectangle(img, (int(width/2)-300,int(height/2)+100), (int(width/2)-100,int(height/2)+300), (255,0,0), 4)

    croppedsize = np.size(cropped7)
    nonzero = np.count_nonzero(cropped7)
    percent = 100*nonzero/croppedsize
    csum = csum + percent
    #print(round(percent), end = " ")

    if percent > great:
        great = percent
        index = 7
    
    startrow, startcol = int(height/2)+100, int(width/2)-100
    endrow, endcol = int(height/2)+300, int(width/2)+100
    cropped8 = maskClose[startrow:endrow, startcol:endcol]
    cv2.rectangle(img, (int(width/2)-100,int(height/2)+100), (int(width/2)+100,int(height/2)+300), (255,0,0), 4)

    croppedsize = np.size(cropped8)
    nonzero = np.count_nonzero(cropped8)
    percent = 100*nonzero/croppedsize
    csum = csum + percent
    #print(round(percent), end = " ")

    if percent > great:
        great = percent
        index = 8
    
    startrow, startcol = int(height/2)+100, int(width/2)+100
    endrow, endcol = int(height/2)+300, int(width/2)+300
    cropped9 = maskClose[startrow:endrow, startcol:endcol]
    cv2.rectangle(img, (int(width/2)+100,int(height/2)+100), (int(width/2)+300,int(height/2)+300), (255,0,0), 4)

    croppedsize = np.size(cropped9)
    nonzero = np.count_nonzero(cropped9)
    percent = 100*nonzero/croppedsize
    csum = csum + percent
    #print(round(percent), end = " ")

    if percent > great:
        great = percent
        index = 9

    if index < 4:        
        drone.set_throttle(40)
        if index == 1:
            drone.set_roll(-40)
        elif index == 3:
            drone.set_roll(40)
        else:
            drone.set_roll(0)
    elif index < 7:
        drone.set_throttle(0)
        if index == 4:
            drone.set_roll(-40)
        elif index == 6:
            drone.set_roll(40)
        else:
            drone.set_roll(0)
    else:
        drone.set_throttle(-40)
        if index == 7:
            drone.set_roll(-40)
        elif index == 9:
            drone.set_roll(40)
        else:
            drone.set_roll(0)
    
    croppedsize = np.size(cropped5)
    nonzero = np.count_nonzero(cropped5)
    percent = 100*nonzero/croppedsize

    if percent > 80.0:
        cv2.rectangle(img, (int(width/2)-100,int(height/2)-100), (int(width/2)+100,int(height/2)+100), (0,255,0), 4)

    if csum <= 80.0:
        drone.set_pitch(40)
    else:
        drone.set_pitch(0)

    drone.move(1)
    
    """cv2.imshow("maskClose",maskClose)
    cv2.imshow("maskOpen",maskOpen)
    cv2.imshow("mask",mask)"""
    cv2.imshow("cam",img)
    """cv2.imshow("1Reference",cropped)
    cv2.imshow("2Reference",cropped2)
    cv2.imshow("3Reference",cropped3)
    cv2.imshow("4Reference",cropped4)
    cv2.imshow("5Reference",cropped5)
    cv2.imshow("6Reference",cropped6)
    cv2.imshow("7Reference",cropped7)
    cv2.imshow("8Reference",cropped8)
    cv2.imshow("9Reference",cropped9)"""
    cv2.waitKey(1)
