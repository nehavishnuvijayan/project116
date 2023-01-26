import cv2
img=cv2.imread("poster.jpg")
cv2.putText(img, "text", (20, 220), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(0,0,255) )
cv2.imshow("output",img)
text="ABC HELLO"
grey_img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.putText(grey_img, text, (20, 220), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(0,0,255) )
cv2.imshow("greyImage",grey_img)
print(img)
cv2.waitKey(0)