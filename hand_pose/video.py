import cv2
import mediapipe as mp
import time



cap = cv2.VideoCapture('data/sample_test1.mp4')
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

# fourcc = cv2.VideoWriter_fourcc(*'MP4V')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('sample_test1_output.mp4',fourcc, 20.0, (1920,1080))

while(cap.isOpened()):
    success, img = cap.read()

    if success == True:

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)
        # print(results.multi_hand_landmarks)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    # print(id, lm)
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)

                    hand_id = [4, 8, 12, 16, 20]
                    if id in hand_id:
                        cv2.circle(img, (cx, cy), 10
                                   , (255, 0, 255), cv2.FILLED)
                        print(id, ' :',cx, cy)

                #mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        # cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
        #             (255, 0, 255), 3)

        cv2.imshow("TEST Image", img)
        out.write(img)
        # cv2.waitKey(1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()