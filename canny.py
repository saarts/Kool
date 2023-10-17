import cv2 as cv

#Tühi funktsioon, trackbar-i callback
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
cv.createTrackbar('Treshold 1',windowName,0,300,on_change)
cv.createTrackbar('Treshold 2',windowName,255,300,on_change)

#Tsükkel
while(True):
    #Võtame hetke väärtused juhtriba pealt
    curTresholdValue1 = cv.getTrackbarPos('Treshold 1',windowName)
    curTresholdValue2 = cv.getTrackbarPos('Treshold 2',windowName)

    #Gaussian Blur
    #resultImg = cv.GaussianBlur(img,(9,9),9,0,9,cv.BORDER_REFLECT101)

    #Median Blur
    resultImg = cv.medianBlur(img,11)

    #Edge detection
    resultImg= cv.Canny(resultImg,curTresholdValue1,curTresholdValue2)

    #Dialate - paksenda
    resultImg = cv.dilate(resultImg,(5,5),iterations=9)

    #Erode - kitsenda
    resultImg = cv.erode(resultImg,(5,5),iterations=4)

    #Näitame pilti
    cv.imshow(windowName,resultImg)

    #Tuvastame nupuvajutuse ja lõpetame tsükli
    key = cv.waitKey(1) & 0xFF
    if key == 27:
        break


#Ootame programmi lõppu
cv.destroyAllWindows()
