from glob import glob
from cv2 import imshow
from imutils.perspective import four_point_transform
import cv2

height = 600
width = 600
green = (0, 255, 0)

coordinates = []
isDrawing = False
working_image = None


def click_event(event, x, y, img):
    global coordinates, isDrawing, working_image
    rect_img = img.copy()
    isDrawing == False
    if event == 0:
        isDrawing = True
    if event == cv2.EVENT_LBUTTONDOWN or event == cv2.EVENT_RBUTTONDOWN:
        print(isDrawing)
        coordinates.append([x, y])
        print(coordinates)
    for i in range(1, len(coordinates)):
        rect_img = cv2.line(img,
                            coordinates[i-1], coordinates[i], (0, 0, 0), 5)
    cv2.imshow("ticket", rect_img)


def cropTicket(filename):

    image = cv2.imread(filename)
    image = cv2.resize(image, (width, height))
    orig_image = image.copy()

    # convert the image to gray scale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imshow('ticket', orig_image)
    cv2.setMouseCallback(
        'ticket', lambda *args: click_event(args[0], args[1], args[2], orig_image))
    cv2.waitKey(0)


cropTicket('./ticket4.jpg')
