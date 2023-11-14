#Enne tuleb YOLO installeerida pip install ultralytics
#Kui tahta GPU kasutada, peab enne YOLO installi pytorchi installi eraldi ära tegema

#võtame YOLO kasutusse
from ultralytics import YOLO
import cv2 as cv

#Laeme mudeli
model = YOLO('yolov8n.pt')

#model.info()

#Söödame mudelile pildi ja saame tulemuse
results = model('joodik.jpg')
#kuna tulemused on jadana, võtame jadast ühe tulemuse
result = results[0]

#Prindime tulemuse objektist boxes objekti sisu
for box in result.boxes:
    print("-------------")
    #Prindime boxes klassi seest tuvastatud objekti kalssi, koordinaadid ja tuvastuskindluse väärtused
    print("Object class: ", box.cls.item())
    print("Object coordinates: ", box.xyxy.tolist())
    print("Object confidence: ", box.conf.item())

#Tsükkel
while(True):
    #Võtame originaalpildi ja joonistame selle peale boxes objekti abil kastid tuvastatud objektide ümber
    #kirjutame klassi nime ja lisame tuvastuskindluse väärtuse
    for box in result.boxes:
        coordinates = box.xyxy[0].tolist()
        coordinates = [round(x) for x in coordinates]
        conf = round(box.conf[0].item(),2)
        class_id = result.names[box.cls[0].item()]
        cv.rectangle(result.orig_img,(coordinates[0],coordinates[1]),(coordinates[2],coordinates[3]),(255,0,0),2)
        cv.putText(result.orig_img,class_id,(coordinates[0],coordinates[1]),cv.FONT_ITALIC,1,(0,0,0),2)
        cv.putText(result.orig_img,str(conf),(coordinates[2],coordinates[3]),cv.FONT_ITALIC,1,(0,0,0),2)

    cv.imshow("tuvastus",result.orig_img)

    key = cv.waitKey(1) & 0xFF
    if key == 27:
        break

cv.destroyAllWindows()

