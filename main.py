import cv2
import mediapipe as mp
import pyautogui
import math
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y=0
index_x=0
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame,1)  ##flip the camera frame
    frame_height, frame_width,_ =frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
          drawing_utils.draw_landmarks(frame,hand)
          landmarks = hand.landmark
          for id, landmark in enumerate(landmarks):
              x = int(landmark.x*frame_width) 
              y = int(landmark.y*frame_height)
              if id == 8: ##index_tip
                    cv2.circle(img=frame,center=(x,y),radius=10,color=(0,255,255))
                    index_x =screen_width/frame_width*x
                    index_y =screen_height/frame_height*y
                    pyautogui.moveTo(index_x,index_y)
              if id == 4: ##leftclick
                    cv2.circle(img=frame,center=(x,y),radius=10,color=(0,255,255))
                    thumb_x =screen_width/frame_width*x
                    thumb_y =screen_height/frame_height*y
                    print('left',abs(index_y - thumb_y))
                    if  math.sqrt((index_x-thumb_x)**2+(index_y-thumb_y)**2)< 20:
                        pyautogui.click()
                        pyautogui.sleep(1)
              if id == 12: ##rightclick
                    cv2.circle(img=frame,center=(x,y),radius=10,color=(0,255,255))
                    middle_x =screen_width/frame_width*x
                    middle_y =screen_height/frame_height*y
                    print('right value',abs(index_y - middle_y))
                    if math.sqrt((index_x-middle_x)**2+(index_y-middle_y)**2) < 20:
                        pyautogui.click(button='right')
                        print("Right Click")
                        pyautogui.sleep(1)
              if id == 20:  ##scrolldown
                  cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                  li_x = screen_width / frame_width *x
                  li_y = screen_height / frame_height *y
                  if abs(thumb_y-li_y)> 500:
                      pyautogui.scroll(20)
                      print(abs(thumb_y-li_y))
                      print("Scrolling uppp!!!")
                  elif abs(index_x-li_x)+(index_y-li_y)< -200 : ###scrollup
                      pyautogui.scroll(-20)
                      print((abs(index_x - li_x) + (index_y - li_y)))
                      print("Scrolling downnn!!! ")                      
    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)

