import cv2 as cv
import time


def on_change(value):

    pass


#Anname pildi aknale nime
windowName = 'Sellel aknal on NIMI!'


#Loeme pildi sisse mustvalgena
img = cv.imread('./balls.jpg',cv.IMREAD_GRAYSCALE)

#Muudame suurust
height,width = img.shape[:2]
img = cv.resize(img,(int(width*0.5),int(height*0.5)),interpolation = cv.INTER_AREA)


#Eelnimetame akna
cv.namedWindow(windowName)

#Lisame juhtribad createTrackbar(trackbarname,winname,value,count,TrackbarCallback,userdata = 0)	
cv.createTrackbar('Treshold',windowName,124,300,on_change)



#Tsükkel

while(True):

    #Võtame hetke väärtused juhtriba pealt
    curTresholdValue1 = cv.getTrackbarPos('Treshold',windowName)



    key = cv.waitKey(1) & 0xFF

    if key == 27:
        break


#Ootame programmi lõppu

cv.destroyAllWindows()
