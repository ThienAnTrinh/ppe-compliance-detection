from ultralytics import YOLO
import cv2
import math

# def video_detection(path_x):
#     video_capture = path_x
#     #Create a Webcam Object
#     cap=cv2.VideoCapture(video_capture)
#     frame_width=int(cap.get(3))
#     frame_height=int(cap.get(4))
#     #out=cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P','G'), 10, (frame_width, frame_height))
#
#     model=YOLO("../YOLO-Weights/yolov8n.pt")
#     classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
#                   "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
#                   "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
#                   "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
#                   "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
#                   "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
#                   "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
#                   "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
#                   "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
#                   "teddy bear", "hair drier", "toothbrush"
#                   ]
#     while True:
#         success, img = cap.read()
#         results=model(img,stream=True)
#         for r in results:
#             boxes=r.boxes
#             for box in boxes:
#                 x1,y1,x2,y2=box.xyxy[0]
#                 x1,y1,x2,y2=int(x1), int(y1), int(x2), int(y2)
#                 print(x1,y1,x2,y2)
#                 cv2.rectangle(img, (x1,y1), (x2,y2), (255,0,255),3)
#                 conf=math.ceil((box.conf[0]*100))/100
#                 cls=int(box.cls[0])
#                 class_name=classNames[cls]
#                 label=f'{class_name}{conf}'
#                 t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
#                 print(t_size)
#                 c2 = x1 + t_size[0], y1 - t_size[1] - 3
#                 cv2.rectangle(img, (x1,y1), c2, [255,0,255], -1, cv2.LINE_AA)  # filled
#                 cv2.putText(img, label, (x1,y1-2),0, 1,[255,255,255], thickness=1,lineType=cv2.LINE_AA)
#         yield img
#         #out.write(img)
#         #cv2.imshow("image", img)
#         #if cv2.waitKey(1) & 0xFF==ord('1'):
#             #break
#     #out.release()
# cv2.destroyAllWindows()

# model = YOLO("weights/best.pt")
#
#
# cap = cv2.VideoCapture(0)
#
# # Loop through the video frames
# while cap.isOpened():
#     # Read a frame from the video
#     success, frame = cap.read()
#     if success:
#         # Run YOLOv8 inference on the frame
#         results = model(frame)
#         # Visualize the results on the frame
#         annotated_frame = results[0].plot()
#         # Display the annotated frame
#         cv2.imshow("Monitoring", annotated_frame)
#         # Break the loop if 'q' is pressed
#         if cv2.waitKey(1) & 0xFF == ord("q"):
#             break
#
# # Release the video capture object and close the display window
# cap.release()
# cv2.destroyAllWindows()

from ultralytics import YOLO
import cv2
import math


def main():

    model = YOLO("weights/best.pt")
    input_path = "static/files/work2.mp4"
    output_path = "detection/output.avi"
    fps = 30
    cap = cv2.VideoCapture(input_path)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(output_path, fourcc, fps, (int(width), int(height)))


    # cap = cv2.VideoCapture(path)
    # # frame_width = int(cap.get(3))
    # # frame_height = int(cap.get(4))
    # # out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*"MJPG"), -1, 20.0, (frame_width, frame_height))
    # fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    # out = cv2.VideoWriter('output.avi', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

    classNames = ["Gloves", "Goggles", "Helmet", "No Glasses", "No Gloves", "No Helmet"]

    while True:
        success, img = cap.read()
        if success:
            results = model(img, stream=True)
            for r in results:
                boxes = r.boxes
                for box in boxes:
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                    print(x1, y1, x2, y2)
                    conf = math.ceil((box.conf[0]*100))/100
                    cls = int(box.cls[0])
                    class_name = classNames[cls]
                    label = f'{class_name}{conf}'
                    t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
                    print(t_size)
                    c2 = x1 + t_size[0], y1 - t_size[1] - 3
                    if cls == 0:
                        color = (0, 255, 10)
                    elif cls == 1:
                        color = (255, 100, 0)
                    elif cls == 2:
                        color = (100, 100, 0)
                    elif cls == 3:
                        color = (0, 100, 255)
                    elif cls == 4:
                        color = (100, 0, 255)
                    elif cls == 5:
                        color = (0, 0, 255)
                    cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
                    cv2.rectangle(img, (x1, y1), c2, color, -1, cv2.LINE_AA)
                    cv2.putText(img, label, (x1, y1-2), 0, 1, [255, 255, 255], thickness=1, lineType=cv2.LINE_AA)

            out.write(img)
            yield img

            #cv2.imshow("image", img)
            if cv2.waitKey(1) & 0xFF==ord('q'):
                break
        else:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
