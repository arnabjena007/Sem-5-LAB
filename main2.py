import cv2
import numpy as np


image_path = 'doggo.jpg'

# Load the image
img = cv2.imread(image_path)

if img is None:
    raise FileNotFoundError(f"Could not load image from '{image_path}'")

# Parameters
gamma = 1.5
C = 20


gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


log_img = C * np.log1p(gray_img.astype(np.float32))


log_img = cv2.normalize(log_img, None, 0, 255, cv2.NORM_MINMAX)
log_img = log_img.astype(np.uint8)


result = cv2.hconcat([gray_img, log_img])


cv2.imshow('Log Transformation', result)


cv2.imwrite('output_image.jpg', result)
print("Output image saved successfully as 'output_image.jpg'")


cv2.waitKey(0)
cv2.destroyAllWindows()