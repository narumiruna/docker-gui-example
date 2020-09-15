import cv2


def read_webcam():
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, img = cap.read()
        if ret:
            yield img
    cap.release()


def main():
    for img in read_webcam():
        cv2.imshow('', img)
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
