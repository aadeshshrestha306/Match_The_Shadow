import mediapipe as mp
import cv2 as cv
import pygame
import sys 

pygame.init()

pygame.display.set_caption("Game")
screen = pygame.display.set_mode((1280, 720))

image = pygame.image.load("bg.jpg")

bg = pygame.transform.scale(image, (1280, 720))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg, (0,0))
    pygame.display.update()


"""    
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

video = 'Gestures\Gestures.mp4'


vidcap = cv.VideoCapture(video)

winwidth = 480
winheight = 750


with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while vidcap.isOpened():
        ret, frame = vidcap.read()
        if not ret:
            break

        # Convert the BGR image to RGB
        rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

        # Process the frame for hand tracking
        processFrames = hands.process(rgb_frame)

        # Draw landmarks on the frame
        if processFrames.multi_hand_landmarks:
            for lm in processFrames.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, lm, mp_hands.HAND_CONNECTIONS)

        # Resize the frame to the desired window size
        resized_frame = cv.resize(frame, (winwidth, winheight))

        # Display the resized frame
        cv.imshow('Hand Tracking', resized_frame)

        # Exit loop by pressing 'q'
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

vidcap.release()
cv.destroyAllWindows()


"""