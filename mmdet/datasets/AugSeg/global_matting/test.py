from opencv_mat import global_matting, guided_filter
import cv2

img_np = cv2.imread('GT04-image.png')
trimap_np = cv2.imread('GT04-trimap.png', cv2.IMREAD_GRAYSCALE)
alpha_np = global_matting(img_np, trimap_np)
alpha_np = guided_filter(img_np, trimap_np, alpha_np, 10, 1e-5)
cv2.imwrite('GT04-alpha.png', alpha_np)
