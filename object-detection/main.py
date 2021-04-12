"""
Object Detection In OpenCv
"""
import cv2
import cmake
import dlib
class ObjectDetector(object):
    classNames = []
    with open('files/coco.names', 'r') as reader:
        for line in reader.readlines():
            classNames.append(line.rstrip())

    def __init__(self, image, confThreshold=.5):
        self.image = image
        self.confThreshold = confThreshold
        self.weightsPath = 'files/frozen_inference_graph.pb'
        self.configPath = 'files/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
        self.inputMean = [(i - i + 1) * 127.5 for i in range(1, 4)]
        self.network = cv2.dnn_DetectionModel(self.weightsPath, self.configPath)
        self.network.setInputSize(320, 320)
        self.network.setInputScale(1.0 / 127.5)
        self.network.setInputMean(tuple(self.inputMean))
        self.network.setInputSwapRB(True)

    def detectObjects(self):
        classIds, confidences, bbox = self.network.detect(self.image, confThreshold=0)

        for classId, confidence, bbx in zip(classIds, confidences, bbox):
            if confidence > .6:
                cv2.rectangle(self.image, tuple(bbx[:2]), (bbx[2] + bbx[0], bbx[1] + bbx[3]), (0, 255, 0), 2)
                cv2.rectangle(self.image, (bbx[0] - 1, bbx[1]), (bbx[2] + bbx[0] + 1, bbx[1] - 20), (0, 255, 0), -1)
                cv2.putText(self.image, f'{self.classNames[classId[0] - 1].upper()}', (bbx[0] + 2, bbx[1] - 5),
                            cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 2)
                # cv2.putText(image, f'{int(confidence[0]*100)} %',(int(bbx[0]+ .80 * bbx[2]), bbx[1]-5), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 2)
        return self.image

# image = cv2.imread("images/image.png")
# image = cv2.resize(image, (int(image.shape[0] * .5), int(image.shape[1] * .5)))

cap = cv2.VideoCapture('videos/Road_traffic_video2.mp4')
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 500)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)
fps = cap.get(cv2.CAP_PROP_FPS)

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.resize(frame, (int(frame.shape[1]*.7), int(frame.shape[0]*.7)), )
    detector = ObjectDetector(frame, confThreshold=.5)
    cv2.imshow("Road", detector.detectObjects())

    if cv2.waitKey(1) & 0xFF == 27:
        cap.release()
        cv2.destroyAllWindows()
        break
