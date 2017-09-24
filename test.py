import numpy as np
from PIL import ImageGrab
import cv2
import time
from keyPress import PressKey,ReleaseKey, UP, DOWN
from alexnet import alexnet

WIDTH = 180
HEIGHT = 100
LR = 1e-3
EPOCHS = 10
MODEL_NAME = 'chrome-tRex-{}-{}-{}-epochs.model'.format(LR, 'alexnetv3',EPOCHS)


def trexJump():
    PressKey(UP)
    ReleaseKey(UP)


def trexDuck():
    PressKey(DOWN)
    ReleaseKey(DOWN)


model = alexnet(WIDTH, HEIGHT, LR)
model.load(MODEL_NAME)


def main():
    last_time = time.time()

    for i in list(range(4))[::-1]:
        print(i + 1)
        time.sleep(1)

    while (True):
        # 800x600 windowed mode
        screen = np.array(ImageGrab.grab(bbox=(0, 95, 600, 270)))
        print('loop took {} seconds'.format(time.time() - last_time))
        last_time = time.time()
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        screen = cv2.resize(screen, (180, 100))
        cv2.imshow('window', screen)
        moves = list(np.around(model.predict([screen.reshape(180, 100, 1)])[0]))
        print(moves)

        if moves == [1, 0, 0]:
            trexJump()
        elif moves == [0, 1, 0]:
            trexDuck()
        elif moves == [0, 0, 1]:
            pass

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


main()