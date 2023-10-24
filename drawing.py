import cv2 as cv

def on_change(value):
    pass

#Anname pildi aknale nime
windowName = 'Sellel aknal on NIMI!'

#Eelnimetame akna
cv.namedWindow(windowName)
#Lisame juhtribad createTrackbar(trackbarname,winname,value,count,TrackbarCallback,userdata = 0)	
cv.createTrackbar('Treshold 1',windowName,0,300,on_change)
cv.createTrackbar('Treshold 2',windowName,255,300,on_change)

#Tsükkel
while(True):

    #Loeme pildi sisse mustvalgena
    img = cv.imread('./balls.jpg',cv.IMREAD_GRAYSCALE)
    #Muudame suurust
    height,width = img.shape[:2]
    scalingFactor = 0.5
    newHeight = int(height*scalingFactor)
    newWidth = int(width*scalingFactor)
    sizedimg = cv.resize(img,(newWidth,newHeight),interpolation = cv.INTER_AREA)

    #Võtame hetke väärtused juhtriba pealt
    curTresholdValue1 = cv.getTrackbarPos('Treshold 1',windowName)
    curTresholdValue2 = cv.getTrackbarPos('Treshold 2',windowName)

    #Alustab puhtalt pildilt
    resultimg = sizedimg

    #Joone joonistamine
    # cv.line(image, start_point, end_point, color, thickness) 
    cv.line(resultimg,(20,20),(100,0),(50,0,0),10)

    #Ristkülik
    #cv.rectangle(image, start_point, end_point, color, thickness)
    cv.rectangle(resultimg, (100,60), (250,300), (24,0,0), 5)

    #Ring
    #cv.circle(image, start_point, radius, color, thickness)
    cv.circle(resultimg, (100,60), 40, (120,0,0), 3)    

    #cv.ellipse(image, centerCoordinates, axesLength, angle, startAngle, endAngle, color , thickness)
    cv.ellipse(resultimg, (200,300), (75,20), 20, 50, 300, (175,0,0), 7)

    #cv.drawMarker(img, (x, y), color, markerType, markerSize, thickness)
    cv.drawMarker(resultimg, (350,350), (67,0,0), cv.MARKER_TRIANGLE_UP, 20, 5)
    
    #cv.putText(image, text, org, font, fontScale, color, thickness)
    cv.putText(resultimg, "SEE on TeksT", (40,400), cv.FONT_ITALIC, 2, (0,0,0), 3)
    cv.putText(resultimg, str(curTresholdValue2), (100,450), cv.FONT_ITALIC, 2, (0,0,0), 3)

    #Näitame pilti
    cv.imshow(windowName,resultimg)

    #Tuvastame nupuvajutuse ja lõpetame tsükli
    key = cv.waitKey(1) & 0xFF
    if key == 27:
        break


#Ootame programmi lõppu
cv.destroyAllWindows()
