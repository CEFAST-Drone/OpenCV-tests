# This hero's code (stack functions): https://github.com/nkmk/python-snippets/blob/e5d988b84b04acfbfd15105546c93c2465f2d126/notebook/opencv_hconcat_vconcat_np_tile.py#L57-L64

import cv2
import numpy as np

def vconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):
    w_min = min(im.shape[1] for im in im_list)
    im_list_resize = [cv2.resize(im, (w_min, int(im.shape[0] * w_min / im.shape[1])), interpolation=interpolation)
                      for im in im_list]
    return cv2.vconcat(im_list_resize)

def hconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):
    h_min = min(im.shape[0] for im in im_list)
    im_list_resize = [cv2.resize(im, (int(im.shape[1] * h_min / im.shape[0]), h_min), interpolation=interpolation)
                      for im in im_list]
    return cv2.hconcat(im_list_resize)

def concat_tile(im_list_2d):
    return cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in im_list_2d])

def concat_tile_resize(im_list_2d, interpolation=cv2.INTER_CUBIC):
    im_list_v = [hconcat_resize_min(im_list_h, interpolation=cv2.INTER_CUBIC) for im_list_h in im_list_2d]
    return vconcat_resize_min(im_list_v, interpolation=cv2.INTER_CUBIC)

img = cv2.imread("test-resources/street.jpg")

im_tile_resize = concat_tile_resize([[img],
                                     [img, img, img, img, img],
                                     [img, img, img]])

img = cv2.resize(img, (373, 199)) # Resizing to get smaller image

imgHor = np.hstack((img, img, img)) # Horizontally stack
imgVer = np.vstack((img, img)) # Horizontally stack

cv2.imshow("Horizontal", imgHor)
cv2.imshow("Vertical", imgVer)
cv2.imshow("Stack", im_tile_resize)

cv2.waitKey(0)