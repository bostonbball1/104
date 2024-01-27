import cv2
img=cv2.imread("solar-sytem.jpg")
cv2.putText(img,"sun",(100,80),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255))
cv2.imshow("output",img)
cv2.waitKey(0)
cv2.imwrite("solar_systemwithname.jpg",img)
