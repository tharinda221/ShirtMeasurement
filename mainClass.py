from tkMessageBox import askyesno, showwarning, showinfo


__author__ = 'tharinda'

import numpy as np
import cv2
import math

count = 0
measure = [[0 for x in range(2)] for x in range(2)]

def onmouseOutput(event, x, y, flags,param):
        global output, count,measure

        # output[x][y]==RED
        if event == cv2.EVENT_LBUTTONDOWN:
            print("X:" + repr(x) + "Y:" + repr(y))
            measure[int(count)][0] = (int(x))
            measure[int(count)][1] = (int(y))
            count += 1


class mainClass:

    global count
    global measure
    def __init__(self):
        pass



    @classmethod
    def mainMethod(event, filename):
        global count,measure
        img = cv2.imread(filename)
        img2 = img.copy()  # a copy of original image
        mask = np.zeros(img.shape[:2], dtype=np.uint8)  # mask initialized to PR_BG
        output = np.zeros(img.shape, np.uint8)  # output image to be shown
        #resized_image=img
        resized_image = cv2.resize(img, (500, 667))
        #resized_image = cv2.resize(img, (0,0), fx=0.20425, fy=0.20435)
        # input windows
        cv2.namedWindow('input')
        cv2.setMouseCallback('input',onmouseOutput)
        cv2.moveWindow('input', img.shape[1] + 10, 90)

        count=0
        while (1):

            cv2.imshow('input', resized_image)
            k = 0xFF & cv2.waitKey(1)

            # key bindings
            if count == 2:  # esc to exit
                break


            elif k == ord('f'):


                print(measure[0][1])
                print(measure[1][1])
            mask2 = np.where((mask == 1) + (mask == 3), 255, 0).astype('uint8')
            output = cv2.bitwise_and(img2, img2, mask=mask2)
            greenImg = output

        cv2.destroyAllWindows()
        x1=measure[0][0]
        x2=measure[1][0]
        y1=measure[0][1]
        y2=measure[1][1]
        dist = math.hypot(x2 - x1, y2 - y1)
        ans=(dist/207)*62
        print repr(round(ans,2))+"cm"
        cv2.destroyAllWindows()
        return repr(round(ans,2))+"cm"
#mainClass=mainClass()
#mainClass.mainMethod("cupz.jpg")