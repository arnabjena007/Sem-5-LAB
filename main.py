import cv2

image_path = 'doggo.jpg'
img = cv2.imread(image_path)

if img is None:
    raise FileNotFoundError(f"Failed to load image: {image_path}")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

neg_img = cv2.bitwise_not(gray_img)

cv2.imshow('Input Image', img)
cv2.imshow('Negative Image', neg_img)

key = cv2.waitKey(0)

if key == ord('s'):
    cv2.imwrite('negative_image.jpg', neg_img)
    print("Negative image saved as 'negative_image.jpg'")

cv2.destroyAllWindows()