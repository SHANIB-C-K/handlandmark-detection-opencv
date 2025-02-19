import cv2 as cv
import mediapipe.python.solutions.hands as mpHands
import mediapipe.python.solutions.drawing_utils as drawing

# camera setup
video = cv.VideoCapture(0)

while True:
    # read frame from camera
    success, frame = video.read()

    # check if camera is working proper or not
    if not success:
        print("Cannot br connect on camera")
        break

    # Camera showing section
    cv.imshow("HandlandMark detection", frame)

    # set if i clicked q button then close the video window
    if cv.waitKey(1) == ord('q'):
        break

cv.destroyAllWindows()