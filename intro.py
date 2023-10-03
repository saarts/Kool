#Impordime OpenCV
import cv2 as cv
#Impordime numpy
import numpy as np

#Pildi kuva - pilt samas kataloogis, kus kood
img = cv.imread('PILT.png')

#Protsessitud pilt
processedImage = cv.cvtColor(img,cv.COLOR_BGR2HSV)

#suuruse muutmine
img = cv.resize(img,(500,500),interpolation = cv.INTER_AREA)
processedImage = cv.resize(processedImage,(500,500),interpolation = cv.INTER_AREA)

#Kombineerime mõlemad pildid
combi = np.concatenate((img,processedImage),axis=0)

#näitame pilti
cv.imshow('Processed',combi)

#ootame nupu vajutust
cv.waitKey(0)

#Kõikide akende sulgemine
cv.destroyAllWindows()


