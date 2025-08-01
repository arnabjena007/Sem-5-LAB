import cv2


cap = cv2.VideoCapture('video.mp4')


while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Video', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:

        break

# Release resources
cap.release()
cv2.destroyAllWindows()