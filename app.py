import cv2
import random

PATH = 'cats/'

def selectImage():
    animalSelector = random.randint(0,1000)
    findin = PATH + str(animalSelector) + '.jpg'
    print(findin)
    return findin

def genImage(imgName):
    image = cv2.imread(imgName)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    detector = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
    rects = detector.detectMultiScale(gray, 1.1, 10, 0, (70, 70))
    for (i, (x, y, w, h)) in enumerate(rects):
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(image, "Cat #{}".format(i + 1), (x, y - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
    cv2.imshow('image',image)
    cv2.waitKey()


if __name__ == '__main__': 
    genImage(selectImage())


