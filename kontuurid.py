import cv2 as cv
import time


def on_change(value):

    pass


#Anname pildi aknale nime

windowName = 'Sellel aknal on NIMI!'


#Loeme pildi sisse mustvalgena

img = cv.imread('./poldid.jpg',cv.IMREAD_GRAYSCALE)

#Muudame suurust

height,width = img.shape[:2]

img = cv.resize(img,(int(width*1.5),int(height*1.5)),interpolation = cv.INTER_AREA)


#Eelnimetame akna

cv.namedWindow(windowName)

#Lisame juhtribad createTrackbar(trackbarname,winname,value,count,TrackbarCallback,userdata = 0)	

cv.createTrackbar('Treshold',windowName,124,300,on_change)



#Tsükkel

while(True):

    #Võtame hetke väärtused juhtriba pealt

    curTresholdValue1 = cv.getTrackbarPos('Treshold',windowName)

    #Eeltöötlus
    resultimg = cv.medianBlur(img,11)

    #Treshold
    retVal, resultimg = cv.threshold(resultimg, curTresholdValue1, 255, cv.THRESH_BINARY_INV)

    #Leiame kontuuride arvu ja asukoha
    #cv.findContours(	image, mode, method[, contours[, hierarchy[, offset]]]	)->	image, contours, hierarchy
    contours,hierarchy = cv.findContours(resultimg,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

    nrofcontours = len(contours)
    #print("Total nr of contours detected: ", nrofcontours)

    nrofcontoursfiltered = 0
    for contour in contours:
        contourarea = cv.contourArea(contour)
        if contourarea > 2000.0:
            nrofcontoursfiltered += 1
            x,y,w,h = cv.boundingRect(contour)
            cv.rectangle(resultimg,(x,y),(x+w,y+h),(150,0,0),1)

    cv.putText(resultimg,"Leitud:",(10,30),cv.FONT_ITALIC,1.25,(255,0,0),1)
    cv.putText(resultimg,str(nrofcontours),(150,30),cv.FONT_ITALIC,1.25,(255,0,0),1)
    cv.putText(resultimg,"Filtreeritud:",(10,70),cv.FONT_ITALIC,1.25,(255,0,0),1)
    cv.putText(resultimg,str(nrofcontoursfiltered),(240,70),cv.FONT_ITALIC,1.25,(255,0,0),1)

    #print("Total of NOICE contours detected: ", nrofcontoursfiltered)
    #Näitame pilti
    cv.imshow(windowName,resultimg)

    time.sleep(0.1)

    #Ootame nupuvajutust
    key = cv.waitKey(1) & 0xFF
    if key == 27:
        break


#Programmi lõpp
cv.destroyAllWindows()
