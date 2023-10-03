import cv2 as cv
import numpy as np

#Pildi kuva
img = cv.imread('./PORR.png')

#Protsessitud pilt
processedImage = cv.cvtColor(img,cv.COLOR_BGR2HSV)

#suuruse muutmine
img = cv.resize(img,(500,500),interpolation = cv.INTER_AREA)
processedImage = cv.resize(processedImage,(500,500),interpolation = cv.INTER_AREA)

combi = np.concatenate((img,processedImage),axis=0)

#näitame pilti
cv.imshow('Processed',combi)

#ootame nupu vajutust
cv.waitKey(0)

cv.destroyAllWindows()


