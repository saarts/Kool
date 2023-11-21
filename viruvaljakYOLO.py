import cv2 as cv
from ultralytics import YOLO
import time
import requests
import numpy as np

#Initsialiseerime yolo mudeli
model = YOLO('yolov8n.pt')



while True:
    
    #Võtame timestampi
    ts = time.time()
    ts = round(ts)
    print(ts)

    #Konstrueerime URL-i
    url = "https://ristmikud.tallinn.ee/last/cam103.jpg?="+str(ts)

    #Requestime raami
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    frame = cv.imdecode(img_arr, -1)

    #Jooksutame mudeli
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

    cv.imshow('Video aken',result.orig_img)

    key = cv.waitKey(1) & 0xFF
    if key == 27:
        break

cv.destroyAllWindows()

