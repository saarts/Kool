import cv2 as cv
from ultralytics import YOLO


#Initsialiseerime yolo mudeli
model = YOLO('yolov8n.pt')

#Määrame video allika

#Allikaks on video fail
capture = cv.VideoCapture('LOL.mp4')

###########Allikaks on võimalusel webcam
###########capture = cv.VideoCapture(0)

#Kontorllime, kas video on korras
if not capture.isOpened():
    print("Something blew up... capture not opened")
    exit()

#Käime video raam raami haaval läbi
while True:
    #Saame raami
    ret, frame = capture.read()

    #Kontrollime kas raam tuli hästi 
    if not ret:
        print("Frame return error")
        break

    results = model(frame)
    result = results[0]

    for box in result.boxes:
        coordinates = box.xyxy[0].tolist()
        coordinates = [round(x) for x in coordinates]
        conf = round(box.conf[0].item(),2)
        class_id = result.names[box.cls[0].item()]
        cv.rectangle(result.orig_img,(coordinates[0],coordinates[1]),(coordinates[2],coordinates[3]),(255,0,0),2)
        cv.putText(result.orig_img,class_id,(coordinates[0],coordinates[1]),cv.FONT_ITALIC,1,(0,0,0),2)
        cv.putText(result.orig_img,str(conf),(coordinates[2],coordinates[3]),cv.FONT_ITALIC,1,(0,0,0),2)

    cv.imshow('Video aken',frame)

    key = cv.waitKey(1) & 0xFF
    if key == 27:
        break

capture.release()
cv.destroyAllWindows()

