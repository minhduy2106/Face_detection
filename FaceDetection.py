import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpFaceDetection = mp.solutions.face_detection
faceDetection = mpFaceDetection.FaceDetection(0.5)
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = faceDetection.process(imgRGB)
    if result.detections:
        for id,detection in enumerate(result.detections):
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, ic = img.shape
            bbox = int(bboxC.xmin * iw), int(bboxC.ymin*ih), int(bboxC.width * iw), int (bboxC.height * ih)
            cv2.rectangle(img, bbox, (255,0,255), 2)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (10, 40), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), thickness=2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
