import numpy as np
import cv2
from src.colors import Colors

# varaible n is the number of squares for each side of the chessboard
n = int(input("How many squares per side do you want in your chessboard? ( n X n ): "))
print("Image dimensions: ")
print("50 pixel multiplied", n, "=", (50 * n), "x",(50 * n) )

# creation an image made of n squares of 50 x 50 pixel
image = np.zeros(((50 * n), (50 * n), 3), dtype="uint8")
# show the empty image
cv2.imshow("Empty chessboard", image)
# press any key to continue
cv2.waitKey()

# function that creates a row of alternating colored squares
def made_row(n):
    # points (x, y) STARTING COORDINATES VALUE of the SQUARE
    # p1 top left point coordinates in the rectangle
    # p2 bottom right point coordinates in the rectangle
    xp1 = 0
    yp1 = 0 + (50 * int(e))
    xp2 = 50
    yp2 = 50 + (50 * int(e))
    # color value inside the row (inside the function made_row)
    colors = color
    for i in range(n):
        # debugghing
        print("round", i)
        # debugging
        print(" color = ", colors)
        # drawing the rectangle of the chessboard
        cv2.rectangle(image,(xp1,yp1),(xp2,yp2), colors, thickness=-1, lineType=cv2.LINE_AA)
        # alternate the color
        colors = Colors.RED if colors == Colors.WHITE else Colors.WHITE
        print("xp1 = ", xp1)
        print("yp1 = ", yp1)
        print("xp2 = ", xp2)
        print("yp2 = ", yp2)
        # increase coordinates of 50 pixel every step on X axis
        xp1 = xp1 + 50
        #yp1 = yp1
        xp2 = xp2 + 50
        #yp2 = yp2
        # debugging
        print(" ------------- ")
        print()

# starting value of stepper for Y shift
e = 0
color = Colors.WHITE
# shifting on Y axis
for shifting in range (n):
    print("shift on Y: ", e)
    made_row(n)
    # stepper increase
    e = e+ 1
    # alternate the color
    color = Colors.RED if color == Colors.WHITE else Colors.WHITE
    print ("incremented e = ", e)
    print(" ***************** ")
    print()
    print()

# show chessboard image
cv2.imshow("Chessboard", image)
# press any key to close all windows
cv2.waitKey()
