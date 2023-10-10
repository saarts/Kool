import cv2 as cv

#Juhtriba callback funktsioon, mida me ei kasuta
def on_change(value):
    pass

#Anname pildi aknale nime
windowName = 'Akna nimi on: "Peeter, Peeter Saar?"'

#Loeme pildi sisse mustvalgena
img = cv.imread('./PORR.png',cv.IMREAD_GRAYSCALE)
#Muudame suurust
height,width = img.shape[:2]
img = cv.resize(img,(int(width*0.5),int(height*0.5)),interpolation = cv.INTER_AREA)

#Eelnimetame akna
cv.namedWindow(windowName)
#Lisame juhtriba createTrackbar(trackbarname,winname,value,count,TrackbarCallback,userdata = 0)	
cv.createTrackbar('Treshold',windowName,127,255,on_change)

#Tekitame tsükli
while(True):
    #Võtame hetke läve väärtuse juhtriba pealt
    curTresholdValue = cv.getTrackbarPos('Treshold',windowName)

    #cv.threshold(	src, thresh, maxval, type[, dst]	) ->	retval, dst
    #cv.THRESH_BINARY #cv.THRESH_BINARY_INV #cv.THRESH_TRUNC #cv.THRESH_TOZERO #cv.THRESH_TOZERO_INV
    retVal,resultImg = cv.threshold(img,curTresholdValue,255,cv.THRESH_TOZERO_INV)

    #Näitame pilti
    cv.imshow(windowName,resultImg)

    #Tuvastame nupuvajutuse ja lõpetame tsükli
    key = cv.waitKey(1) & 0xFF
    if key == 27:
        break


#Ootame programmi lõppu, et hävitada kõik aknad
cv.destroyAllWindows()
