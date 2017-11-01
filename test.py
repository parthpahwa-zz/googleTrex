import cv2
import time
from Utils.keyPress import *
from Utils.alexnet import alexnet
from Utils.getScreen import grab_screen

WIDTH = 200
HEIGHT = 70
screenRegion = (30, 130, 610, 250)
LR = 1e-3
EPOCHS = 15
MODEL_NAME = 'chrome-tRex-{}-{}-{}-epochs.model'.format(LR, 'alexnet', EPOCHS)
model = alexnet(WIDTH, HEIGHT, LR)
model.load(MODEL_NAME)


def trexJump():
    PressKey(UP)
    PressKey(UP)
    PressKey(UP)
    PressKey(UP)
    PressKey(UP)
    PressKey(UP)
    PressKey(UP)
    PressKey(UP)
    ReleaseKey(UP)


def main():
    for i in list(range(4))[::-1]:
        print(i + 1)
        time.sleep(1)

    while 1:

        # Capture the required region of the screen and convert to greyscale
        screen = grab_screen(region=screenRegion)
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

        # resize to something a bit more acceptable for a CNN
        screen = cv2.resize(screen, (HEIGHT, WIDTH))
        moves = list(model.predict([screen.reshape(200, 70, 1)])[0])

        if moves[0] > 0.50:
            trexJump()
        else:
            pass


main()
