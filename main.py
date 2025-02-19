import cv2 as cv
import mediapipe.python.solutions.hands as mpHands
import mediapipe.python.solutions.drawing_utils as drawing

# hands object section
hands = mpHands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
)

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
    frame = cv.flip(frame, 1)
    # Convert the BGR image to RGB image
    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    # handdetect section
    results = hands.process(rgb_frame)

    # check if results landmark
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # draw landmark on frame
            drawing.draw_landmarks(
                image=frame,
                landmark_list=hand_landmarks,
                connections=mpHands.HAND_CONNECTIONS,
            )
        
    
    # exit text on window
    cv.putText(frame, "Press 'q' to exit", (10, 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv.imshow("HandlandMark detection", frame)

    # set if i clicked q button then close the video window
    if cv.waitKey(1) == ord('q'):
        break
