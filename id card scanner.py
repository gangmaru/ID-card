import pytesseract
import cv2

card_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

path='idcard.png'
img = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
rgb_image=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

cards = card_cascade.detectMultiScale(gray, 1.1, 6)
text=pytesseract.image_to_string(rgb_image,lang='kor')

print(text)

for(x,y,w,h) in cards:
    print(x, y, w, h)
    cv2.rectangle(img, (x,y), (x + w, y + h), (255, 0, 0), 2)    

cv2.imshow('img', img)
cv2.waitKey()