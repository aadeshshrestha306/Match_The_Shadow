import mediapipe as mp
import cv2 as cv
import pygame
import sys 

pygame.init()

pygame.display.set_caption("Match Fruits")
screen = pygame.display.set_mode((1280, 720))

image = pygame.image.load("Resources/wallpaper.jpg")

bg = pygame.transform.scale(image, (1280, 720))

f1 = pygame.image.load("Resources/Fruits/apple.jpg")
f2 = pygame.image.load("Resources/Fruits/banana.png")


apple = pygame.transform.scale(f1, (200,256))
banana = pygame.transform.scale(f2, (200,200))


apple_shadow = pygame.Surface(apple.get_size(), pygame.SRCALPHA)
banana_shadow = pygame.Surface(banana.get_size(), pygame.SRCALPHA)


shadow_alpha = 100
apple_shadow.fill((0, 0, 0, shadow_alpha))
banana_shadow.fill((0, 0, 0, shadow_alpha))


# Define fruit positions
apple_pos = (100, 100)
banana_pos = (300, 100)

# Main game loop
dragging = False
dragged_fruit = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if apple.get_rect(topleft=apple_pos).collidepoint(event.pos):
                dragging = True
                dragged_fruit = apple
            elif banana.get_rect(topleft=banana_pos).collidepoint(event.pos):
                dragging = True
                dragged_fruit = banana
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
            dragged_fruit = None

    screen.fill((255, 255, 255))

    # Draw shadows
    screen.blit(bg, (0,0))

    screen.blit(apple, apple_pos)
    screen.blit(banana, banana_pos)

    # Drag and drop logic
    if dragging and dragged_fruit:
        dragged_fruit_rect = dragged_fruit.get_rect(topleft=pygame.mouse.get_pos())
        screen.blit(dragged_fruit, dragged_fruit_rect.topleft)

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