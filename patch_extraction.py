#!/usr/bin/python

import sys
import cv2
import numpy as np
import os

img_file = sys.argv[1]
patch_size = int(sys.argv[2])
coordx = float(sys.argv[3])
coordy = float(sys.argv[4])
out_folder = sys.argv[5]
out_index = sys.argv[6]


img_file_w_ext = os.path.basename(img_file)
img_file_name,img_file_ext = os.path.splitext(img_file_w_ext)
 
image = cv2.imread(img_file)
image_h = image.shape[0]
image_w = image.shape[1]

coordx = int(image_w*coordx)
coordy = int(image_h*coordy)

patch_center = np.array([coordy, coordx])
patch_x = int(patch_center[0] - patch_size / 2.)
patch_y = int(patch_center[1] - patch_size / 2.)
patch_image = image[patch_x:patch_x+patch_size, patch_y:patch_y+patch_size]

cv2.imwrite(out_folder+"/"+img_file_name+"_"+os.path.basename(os.path.normpath(out_folder))+"_patch_"+out_index+".png",patch_image)
