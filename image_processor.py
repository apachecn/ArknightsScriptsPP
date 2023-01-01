import os
import time
import re
import cv2
import easyocr
from PIL import Image

import settings


last_match_loc = None

def match_template(target_path,template_path,threshold = 0.05,return_center = True
					,print_debug = True,scope = None,except_locs = None):

	if(print_debug):
		print("ImageProcessor: start to match "+target_path+" by "+template_path)

	if(print_debug and except_locs != None):
		print("ImageProcessor: except_locs: "+str(except_locs))

	target = cv2.imread(target_path)
	template = cv2.imread(template_path)
	theight, twidth = template.shape[:2]

	if(scope != None):
		target = target[scope[0]:scope[1],scope[2]:scope[3]]

	result = cv2.matchTemplate(target,template,cv2.TM_SQDIFF_NORMED)

	len1, len2 = result.shape[:2]
	if(except_locs != None):
		for except_loc in except_locs:
			if(except_loc == None):
				continue
			for j in range(except_loc[0] - settings.except_dist,except_loc[0] + settings.except_dist):
				for k in range(except_loc[1] - settings.except_dist,except_loc[1] + settings.except_dist):
					if(j>=0 and j<len2 and k>=0 and k<len1):
						result[k][j] = 1

	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

	if(print_debug):
		print("ImageProcessor: best match value :"+str(min_val)+"   match location:"+str(min_loc[0])+" "+str(min_loc[1]))
	
	if(min_val > threshold):
		if(print_debug):
			print("ImageProcessor: match failed")
		return None
	else:
		if(print_debug):
			print("ImageProcessor: match succeeded")

	last_match_loc = min_loc

	if(return_center):
		min_loc = (min_loc[0] + twidth/2,min_loc[1] + theight/2)

	if(scope != None):
		min_loc = (min_loc[0] + scope[2],min_loc[1] + scope[0])

	return min_loc


def easyocr_read(target_path,print_debug = True,scope = None):

	reader = easyocr.Reader(['ch_sim','en'], gpu = False)
	target = cv2.imread(target_path) 

	if(scope != None):
		target = target[scope[0]:scope[1],scope[2]:scope[3]]

	result = reader.readtext(target)

	if(print_debug):
		for reline in result:
			print(reline)

	return result
