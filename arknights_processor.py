import os
import time
import re
import cv2
import random

import settings
import image_processor
import adb_controller

def stop_app():
	print("ArknightsController:Stop the App  ....")
	adb_controller.stop_app()

def start_app():
	print("ArknightsController:Start the App  ....")
	re = adb_controller.wait_to_match_and_click([r"template_images\start0.png"],[0.01],True,60,2)
	if(re == "restart"):return re

	print("ArknightsController:Wait to click Yellow Start Button  ....")
	time.sleep(5)
	re = adb_controller.wait_to_match_and_click([r"template_images\start1.png"],[0.15],True,300,1.123)
	if(re == "restart"):return re

	print("ArknightsController:Wait to click Start Wake Button  ....")
	time.sleep(5)
	re = adb_controller.wait_to_match_and_click([r"template_images\start2.png"],[0.05],True,30,1.123)
	if(re == "restart"):return re

	print("ArknightsController:Wait to get in Main Page  ....")
	re = adb_controller.wait_till_match_any([r"template_images\level0.png"],[0.05],True,60,3,settings.accidents)
	if(re == "restart"):return re


def restart_app():
	print("ArknightsController:Start to Restart  ....")
	stop_app()
	start_app()

def go_level():
	
	print("ArknightsController:Start to run Level  ....")

	#get to the level
	re  = adb_controller.wait_to_match_and_click([r"template_images\level0.png"],[0.05],True,20,1,settings.accidents)
	if(re == "restart"):return re

	success_in_t_level = False
	last_t_level_image = ""
	if(len(settings.auto_t_level) > 0):#temp level
		for temp_image in settings.auto_t_level :
			last_t_level_image = temp_image
			re = adb_controller.wait_to_match_and_click([temp_image],[0.1],True,30,1)
			re = adb_controller.wait_to_match_and_click([temp_image],[0.1],True,5,1)
			if(re == "success"):
				success_in_t_level = True
			else:
				success_in_t_level = False

	if(success_in_t_level == False):#temp failed

		re = adb_controller.wait_to_match_and_click(
					[r"template_images\level1.png"
					,r"template_images\level1_2.png"],[0.05,0.05],True,20,1)
		if(re == "restart"):return re

		re = adb_controller.wait_to_match_and_click([r"template_images\level2_ce.png"],[0.05],True,10,1)
		if(re == "success"):#Can Make Money, go ce level
			re = adb_controller.wait_to_match_and_click(
				[r"template_images\level3_ce{}.png".format(settings.auto_ce_level)],[0.05],True,5,1)
			if(re == "restart"):
				return re
			if(re == "failed"):
				adb_controller.swipe((800,400),(400,400),1000)
				time.sleep(1)
				re = adb_controller.wait_to_match_and_click(
					[r"template_images\level3_ce{}.png".format(settings.auto_ce_level)],[0.05],True,10,1)
				if(re == "failed"):
					print("ERROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOR")
					print("ArknightsController:Can not match " 
						+ r"template_images\level3_ce{}.png".format(settings.auto_ce_level))
		else: #Can only make exp,go ls level
			re = adb_controller.wait_to_match_and_click(
				[r"template_images\level2_ls.png"],[0.05],True,20,1)
			if(re == "restart"):return re
			re = adb_controller.wait_to_match_and_click(
				[r"template_images\level3_ls{}.png".format(settings.auto_ls_level)],[0.05],True,20,1)
			if(re == "failed"):
				adb_controller.swipe((800,400),(400,400),1000)
				time.sleep(1)
				re = adb_controller.wait_to_match_and_click(
					[r"template_images\level3_ls{}.png".format(settings.auto_ls_level)],[0.05],True,20,1)
				if(re == "failed"):
					print("ERROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOR")
					print("ArknightsController:Can not match " 
						+ r"template_images\level3_ce{}.png".format(settings.auto_ce_level))

	#repeat the level
	while(True):
		re = adb_controller.wait_to_match_and_click([r"template_images\level8.png"],[0.02],True,6,2)
		if(re == "restart"):return re

		if(success_in_t_level == False):
			re = adb_controller.wait_to_match_and_click([r"template_images\level4.png"],[0.01],True,20,2)
			if(re == "restart"):return re
		else:
			re = adb_controller.wait_to_match_and_click([last_t_level_image],[0.01],True,30,2)
			if(re == "restart"):return re
		
		re = adb_controller.wait_to_match_and_click([r"template_images\level5.png"],[0.01],True,20,2,settings.accidents)
		if(re == "restart"):return re
		if(re == "failed"):return re
		re = adb_controller.wait_till_match_any([r"template_images\level6.png"],[0.01],True,20,1)
		if(re == "restart"):return re
		re = adb_controller.wait_while_match([r"template_images\level6.png"],[0.01],600,10)
		if(re == "restart"):return re

		time.sleep(5)
		re = adb_controller.wait_to_match_and_click([r"template_images\level7.png",r"template_images\level7-2.png"]
			,[0.2,0.2],True,600,2,settings.accidents,click_offset=[300,-300])
		if(re == "failed" or re == "restart"):return "restart"
		re = adb_controller.wait_to_match_and_click([r"template_images\level7.png"],[0.2],True,10,2,settings.accidents)

	print("ArknightsController:Finished go level  ....")	
	return "success"

crew_rects={
	"up_left_loc":[(417,96),(417,360),(561,96),(561,360)
				,(705,96),(705,360),(849,96),(849,360)
				,(993,96),(993,360),(1137,96),(1137,360)]
	,"witdth":123
	,"height":257
}

def go_infrastructure():
	print("ArknightsController:Start to run Infrastructure  ....")
	#get in the Infrastructure
	re  = adb_controller.wait_to_match_and_click([r"template_images\infrastructure1.png"],[0.05],True,20,1,settings.accidents)
	if(re == "restart"):return re
	re = adb_controller.wait_till_match_any([r"template_images\infrastructure2.png"],[0.05],True,20,1)
	if(re == "restart"):return re

	print("ArknightsController:Start to Collect Goods  ....")
	adb_controller.swipe((400,400),(800,400),2000)
	time.sleep(1)

	re = "success"
	while(re == "success"):
		re = adb_controller.wait_to_match_and_click(
			[r"template_images\infrastructure3.png",r"template_images\infrastructure4.png"],[0.05,0.05],True,5,1)

	print("ArknightsController:Check Blue Notification  ....")
	re = adb_controller.wait_to_match_and_click([r"template_images\infrastructure5.png"],[0.05],True,5,3,settings.accidents)
	if(re == "success"):
		print("ArknightsController:Collect Trust  ....")
		re = adb_controller.wait_to_match_and_click([r"template_images\infrastructure6.png"],[0.05],True,10,2,settings.accidents)
		print("ArknightsController:Get Back  ....")
		re = adb_controller.wait_to_match_and_click([r"template_images\infrastructure7.png"],[0.05],True,10,2,settings.accidents)
		re = adb_controller.wait_to_match_and_click([r"template_images\infrastructure7_2.png"],[0.05],True,5,2,settings.accidents)
		print("ArknightsController:Get In  ....")
		re  = adb_controller.wait_to_match_and_click([r"template_images\infrastructure1.png"],[0.05],True,20,1,settings.accidents)
	else:
		print("ArknightsController:Do not find Blue Notification  ....")

	print("ArknightsController:Change the Crew  ....")
	re  = adb_controller.wait_to_match_and_click([r"template_images\infrastructure8.png"],[0.05],True,10,1,accidents = settings.accidents)

	#Get Down
	re  = adb_controller.wait_to_match_and_click([r"template_images\infrastructure9.png"],[0.05],True,10,1,accidents = settings.accidents)
	while(True):#scoll
		matched_locs = []
		re = "success"
		while(re == "success"):
			re  = adb_controller.wait_to_match_and_click(
				[r"template_images\infrastructure10.png"
				,r"template_images\infrastructure11.png"
				,r"template_images\infrastructure11_2.png"
				,r"template_images\infrastructure11_3.png"
				,r"template_images\infrastructure11_4.png"
				]
				,[0.05,0.05,0.05,0.05,0.05],False,5,1,accidents = settings.accidents
				,click_offset = (-20,25),scope = (118,696,618,1226),except_locs = matched_locs)

			if(image_processor.last_match_loc != None):
				matched_locs.append(image_processor.last_match_loc)

		adb_controller.screenshot(r"temp_screenshot\last_screenshot.png")
		adb_controller.swipe((1000,600),(1000,150),2000)
		time.sleep(1)
		adb_controller.screenshot(r"temp_screenshot\screenshot.png")
		if(image_processor.match_template(r"temp_screenshot\last_screenshot.png",r"temp_screenshot\screenshot.png",0.01,False) == (0,0)):
			break


	print("ArknightsController:Finished Laying off the Crew  ....")
	print("ArknightsController:Start to Station the Crew  ....")

	print("ArknightsController:Get Out  ....")
	re = adb_controller.wait_to_match_and_click([r"template_images\infrastructure7.png"],[0.05],True,10,2,settings.accidents)
	print("ArknightsController:Get In  ....")
	re  = adb_controller.wait_to_match_and_click([r"template_images\infrastructure8.png"],[0.05],True,10,1,accidents = settings.accidents)

	#Get On
	while(True):#Repeat Scorll
		matched_locs = []
		re = "success"
		while(re == "success"):
			# adb_controller.screenshot(r"temp_screenshot\last_screenshot.png")
			re  = adb_controller.wait_to_match_and_click(
				[r"template_images\infrastructure13.png"
				,r"template_images\infrastructure13_2.png"
				,r"template_images\infrastructure13_3.png"
				,r"template_images\infrastructure13_4.png"
				,r"template_images\infrastructure13_5.png"
				,r"template_images\infrastructure13_6.png"
				],[0.02,0.02,0.02,0.02,0.02,0.02],True,6,2
				,accidents = settings.accidents,scope = (118,720,618,1226),except_locs = matched_locs)
			
			if(re == "success"):
				matched_locs.append(image_processor.last_match_loc)
				# print("KKK:"+str(matched_locs))
				time.sleep(2)
				clicked_nums = 0
				for rect_index in range(0,len(crew_rects["up_left_loc"])):
					print("ArknightsController: Check rect_index = "+str(rect_index))
					re2 = adb_controller.wait_till_match_any(
						[r"template_images\infrastructure16.png"
						,r"template_images\infrastructure16_2.png"
						,r"template_images\infrastructure16_3.png"
						,r"template_images\infrastructure16_4.png"
						,r"template_images\infrastructure16_5.png"]
						,[0.05,0.05,0.05,0.05,0.05],True,1,1,scope = (
							crew_rects["up_left_loc"][rect_index][1]
							,crew_rects["up_left_loc"][rect_index][1] + crew_rects["height"]
							,crew_rects["up_left_loc"][rect_index][0]
							,crew_rects["up_left_loc"][rect_index][0] + crew_rects["witdth"]
							)
						)
					if(re2 != None):
						print("ArknightsController: Crew "+str(rect_index)+" is already in work/rest")
						continue
					adb_controller.click((crew_rects["up_left_loc"][rect_index][0] + crew_rects["witdth"]/2
						,crew_rects["up_left_loc"][rect_index][1] + crew_rects["height"]/2))
					clicked_nums = clicked_nums + 1
					if(clicked_nums >= 5):
						break

				print("ArknightsController: Current Crew have stationed")

				re2  = adb_controller.wait_to_match_and_click(
					[r"template_images\infrastructure15.png"
					,r"template_images\infrastructure15_2.png"
					],[0.05,0.05],True,10,1,accidents = settings.accidents)
				time.sleep(1)

		adb_controller.screenshot(r"temp_screenshot\last_screenshot.png")
		adb_controller.swipe((1000,600),(1000,150),2000)
		time.sleep(1)
		adb_controller.screenshot(r"temp_screenshot\screenshot.png")

		if(image_processor.match_template(r"temp_screenshot\last_screenshot.png",r"temp_screenshot\screenshot.png",0.01,False) == (0,0)):
			break

	print("ArknightsController:Finished go infrastructure  ....")
	return "success"

def go_visit_friends():
	print("ArknightsController:Start to visit friends  ....")
	re  = adb_controller.wait_to_match_and_click([r"template_images\friends1.png"],[0.05],True,20,2,settings.accidents)
	if(re == "restart"):return re
	re  = adb_controller.wait_to_match_and_click([r"template_images\friends2.png"],[0.05],True,20,2,settings.accidents)
	if(re == "restart"):return re
	re  = adb_controller.wait_to_match_and_click([r"template_images\friends3.png"],[0.05],True,20,2,settings.accidents)
	if(re == "restart"):return re

	visit_times = 1
	while(visit_times < 10):
		adb_controller.click((1174,632))
		time.sleep(3)
		# re  = adb_controller.wait_to_match_and_click([r"template_images\friends4.png"],[0.05],True,20,2,settings.accidents)
		# if(re == "restart" or re == "failed"):return "restart"
		visit_times = visit_times + 1 

	print("ArknightsController:Finished visiting friends  ....")
	return "success"

def go_collect_quests():
	print("ArknightsController:Start to collect quest rewards  ....")
	re  = adb_controller.wait_to_match_and_click([r"template_images\quest1.png"],[0.05],True,10,1,settings.accidents)
	if(re == "restart"):return re
	re  = adb_controller.wait_to_match_and_click([r"template_images\quest2.png"],[0.05],True,10,1,settings.accidents)
	if(re == "restart"):return re

	re  = adb_controller.wait_to_match_and_click([r"template_images\quest3.png"],[0.05],True,10,1,settings.accidents)
	if(re == "restart"):return re
	re  = adb_controller.wait_to_match_and_click([r"template_images\quest2.png"],[0.05],True,10,1,settings.accidents)
	if(re == "restart"):return re

	re  = adb_controller.wait_to_match_and_click([r"template_images\quest4.png"],[0.05],True,10,1,settings.accidents)
	if(re == "restart"):return re
	re  = adb_controller.wait_to_match_and_click([r"template_images\quest2.png"],[0.05],True,10,1,settings.accidents)
	if(re == "restart"):return re

	re  = adb_controller.wait_to_match_and_click([r"template_images\quest5.png"],[0.05],True,10,1,settings.accidents)
	if(re == "restart"):return re
	re  = adb_controller.wait_to_match_and_click([r"template_images\quest2_2.png"],[0.05],True,10,1,settings.accidents)
	if(re == "restart"):return re
	print("ArknightsController:Finished to collect quest rewards  ....")
	return "success"

def go_collect_mail():
	print("ArknightsController:Start to collect mail  ....")
	re  = adb_controller.wait_to_match_and_click([r"template_images\mail1.png"],[0.05],True,10,1,settings.accidents)
	if(re == "restart"):return re
	re  = adb_controller.wait_to_match_and_click([r"template_images\mail2.png"],[0.05],True,10,1,settings.accidents)
	if(re == "restart"):return re
	adb_controller.wait_to_match_and_click([r"template_images\accident_daily_gift.png"],[0.05],True,10,2)

	print("ArknightsController:Finished to collect mail  ....")
	return "success"

def go_shop():
	print("ArknightsController:Start to go shop  ....")
	re  = adb_controller.wait_to_match_and_click([r"template_images\shop1.png"],[0.05],True,10,2,settings.accidents)
	if(re == "restart"):return re
	re  = adb_controller.wait_to_match_and_click([r"template_images\shop2.png"],[0.05],True,10,2,settings.accidents)
	if(re == "restart"):return re
	re  = adb_controller.wait_to_match_and_click([r"template_images\shop3.png"],[0.05],True,10,2,settings.accidents)
	if(re == "restart"):return re
	re  = adb_controller.wait_to_match_and_click([r"template_images\shop7.png"],[0.05],True,10,2,settings.accidents)
	if(re == "restart"):return re

	while(True):
		re  = adb_controller.wait_to_match_and_click(
			[r"template_images\shop4.png",r"template_images\shop5.png"],[0.05,0.05],True,10,2,settings.accidents)
		if(re == "success"):
			adb_controller.wait_to_match_and_click([r"template_images\shop6.png"],[0.05],True,10,2,settings.accidents)
			adb_controller.wait_to_match_and_click([r"template_images\shop7.png"],[0.05],True,10,2,settings.accidents)
		else:
			break

	print("ArknightsController:Finished to shop  ....")
	return "success"

def go_hire_crew():
	print("ArknightsController:Start to hire crew  ....")
	re  = adb_controller.wait_to_match_and_click([r"template_images\hire1.png"],[0.05],True,10,2,settings.accidents)
	if(re == "restart"):return re

	print("ArknightsController:Try to collect crew  ....")
	while(True):
		re  = adb_controller.wait_to_match_and_click([r"template_images\hire2.png"],[0.05],True,10,2,settings.accidents)
		if(re == "success"):
			time.sleep(2)
			re2  = adb_controller.wait_to_match_and_click([r"template_images\hire3.png"],[0.05],True,10,2,settings.accidents)
			time.sleep(2)
			adb_controller.click((1000,300))
		else:
			break

	print("ArknightsController:Try to begin collect crew  ....")
	while(True):
		re  = adb_controller.wait_to_match_and_click(
			[r"template_images\hire4.png"
			,r"template_images\hire4_2.png"
			,r"template_images\hire4_3.png"
			,r"template_images\hire4_4.png"]
			,[0.05,0.05,0.05,0.05],True,10,2,settings.accidents)
		if(re == "success"):
			time.sleep(2)
			re2  = adb_controller.wait_to_match_and_click(
				[r"template_images\hire5.png"],[0.05],False,10,2,settings.accidents,click_offset = (225,180))

			re2 = adb_controller.wait_till_match_any_text(settings.go_hire_stop_options,5,1,scope = (343,500,338,900))
			if(re2 != None):
				print("ArknightsController:Found stop option in {},so stop".format(str(settings.go_hire_stop_options)))
				return "success"

			re2  = adb_controller.wait_to_match_and_click(
				[r"template_images\hire6.png"],[0.05],False,10,2,settings.accidents,click_offset = (195,-12))
			re2  = adb_controller.wait_to_match_and_click(
				[r"template_images\hire7.png"],[0.05],True,10,2,settings.accidents)
		else:
			break

	print("ArknightsController:Finished to hire crew  ....")
	return "success"

def go_clue_get_in():
	re  = adb_controller.wait_to_match_and_click([r"template_images\gclue1.png"],[0.05],True,10,2,settings.accidents)
	re = adb_controller.wait_till_match_any([r"template_images\gclue2.png"],[0.05],True,20,1)
	if(re == "restart"):return re
	adb_controller.swipe((800,400),(400,400),2000)
	re  = adb_controller.wait_to_match_and_click([r"template_images\gclue3.png"],[0.05],True,10,2,settings.accidents)
	re  = adb_controller.wait_to_match_and_click([r"template_images\gclue4.png"],[0.05],True,10,2,settings.accidents)
	
# Require get in first
def go_clue_get_on_clue():
	re  = adb_controller.wait_to_match_and_click([r"template_images\gclue5.png"],[0.05],True,10,2,settings.accidents)
	for tab_index in range(1,8):
		re  = adb_controller.wait_to_match_and_click([r"template_images\gclue6_{}.png".format(tab_index)],[0.1],True,10,2,settings.accidents)
		re = adb_controller.wait_till_match_any(
			[r"template_images\gclue7_1.png",r"template_images\gclue7_2.png"],[0.05,0.05],True,3,1,scope = (148,330,879,1268))
		if(re == None):
			adb_controller.click((1094,238))
	re  = adb_controller.wait_to_match_and_click([r"template_images\gclue11.png"],[0.05],True,10,2,settings.accidents)
	re  = adb_controller.wait_to_match_and_click([r"template_images\gclue4.png"],[0.05],True,10,2,settings.accidents)

def go_send_additional_clue():
	
	re  = adb_controller.wait_to_match_and_click([r"template_images\gclue12.png"],[0.05],True,10,2,settings.accidents)

	for tab_index in range(1,8):

		re  = adb_controller.wait_to_match_and_click(
			[r"template_images\gclue18_{}.png".format(tab_index)],[0.05],True,5,1,settings.accidents)

		if(re == None):
			print("ArknightsController:ERROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOR cannot find number tab  ....")
			return "ERROR"

		re  = adb_controller.wait_to_match_and_click(
			[r"template_images\gclue13.png"],[0.05],True,3,1,settings.accidents,scope = (336,534,14,423))

		if(re == "success"):

			direction = "No"

			while(True):
				re2 = adb_controller.wait_till_match_any(
					[r"template_images\gclue14.png"],[0.01],True,5,1,scope = (68,633,819,1157))
				
				if(re2 == None):

					scroll_result = None

					if(direction == "No" or direction == "right"):
						scroll_result  = adb_controller.wait_to_match_and_click(
							[r"template_images\gclue15.png"],[0.05],True,3,1,settings.accidents,scope = (635,710,1060,1253))
					else:
						scroll_result  = adb_controller.wait_to_match_and_click(
							[r"template_images\gclue16.png"],[0.05],True,3,1,settings.accidents,scope = (635,710,1060,1253))

					if(scroll_result != "success"):
						break
					else:
						continue

				else:
					adb_controller.click((1187,re2[1]))
					break

	re  = adb_controller.wait_to_match_and_click([r"template_images\gclue17.png"],[0.05],True,10,2,settings.accidents)




def go_clue_get_new_clue():
	for repeat_time in range(0,2):
		re  = adb_controller.wait_to_match_and_click(
			[r"template_images\gclue9.png",r"template_images\gclue9_2.png"]
			,[0.05,0.05],False,10,2,settings.accidents,click_offset = (-20,44))
		if(re == "success"):
			re  = adb_controller.wait_to_match_and_click([
				r"template_images\gclue10.png",r"template_images\gclue10_1.png"],[0.05,0.05],True,10,2,settings.accidents)
		else:
			break;


def go_clue():
	print("ArknightsController:Start to Go Clue -- Get in ....")
	go_clue_get_in()

	print("ArknightsController:Start to Go Clue -- Get on new clue  ....")
	go_clue_get_on_clue()

	print("ArknightsController:Start to Go Clue -- Try unlock clue  ....")
	re  = adb_controller.wait_to_match_and_click([r"template_images\gclue8.png"],[0.05],True,10,2,settings.accidents)
	if(re == "success"):
		re  = adb_controller.wait_to_match_and_click([r"template_images\gclue4.png"],[0.05],True,10,2,settings.accidents)

	print("ArknightsController:Start to Go Clue -- Send additional clue  ....")
	go_send_additional_clue()

	print("ArknightsController:Start to Go Clue -- Get new clue  ....")
	go_clue_get_new_clue()

	print("ArknightsController:Finished to Go Clue  ....")
	return "success"

def go_drone():
	print("ArknightsController:Start to Go Drone -- Get in ....")
	re  = adb_controller.wait_to_match_and_click([r"template_images\infrastructure1.png"],[0.05],True,20,1,settings.accidents)
	if(re == "restart"):return re

	adb_controller.swipe((400,400),(800,400),2000)
	time.sleep(2)

	re  = adb_controller.wait_to_match_and_click([r"template_images\drone1.png"],[0.05],True,20,1,settings.accidents)
	if(re != "success"):
		return "end"

	re  = adb_controller.wait_to_match_and_click([r"template_images\drone2.png"],[0.05],True,20,1,settings.accidents)
	if(re != "success"):
		return "end"

	while(True):
		re  = adb_controller.wait_to_match_and_click([r"template_images\drone3.png"],[0.05],True,20,1,settings.accidents)
		if(re != "success"):
			return "end"

		re  = adb_controller.wait_till_match_any([r"template_images\drone7.png"],[0.01],True,4,1)
		if(re != None):
			return "end"

		re  = adb_controller.wait_to_match_and_click([r"template_images\drone4.png"],[0.05],True,20,1,settings.accidents)
		if(re != "success"):
			return "end"

		re  = adb_controller.wait_to_match_and_click([r"template_images\drone6.png"],[0.05],True,20,1,settings.accidents)
		if(re != "success"):
			return "end"
	

	print("ArknightsController:Finished to Go Clue  ....")
	return "success"

	

	


########################  Main   ##########################

settings_path = r"settings.txt"

add_string_vars = ["to_do_list","auto_t_level"]

string_vars = ["adb_path","device_address"]

int_vars = ["auto_ce_level"
				,"auto_ls_level"
				,"go_level_cycle"
				,"go_infrastructure_cycle"
				,"go_visit_friends_cycle"
				,"go_collect_quests_cycle"
				,"go_collect_mail_cycle"
				,"go_shop_cycle"
				,"go_hire_crew_cycle"
				,"go_hire_stop_options"
				,"go_clue_cycle"
				,"go_drone_cycle"
				,"recheck_time_when_no_work_to_do"]
				
print("#####################################################")
print("Start to read settings by {}".format(settings_path))
print("#####################################################")



for add_string_var in add_string_vars:
	exec("settings.{} = []".format(add_string_var),globals())
	# print("clear {}".format(add_string_var))
	# print(str(to_do_list))

for line in open(settings_path,encoding = "gb18030",errors = "ignore"):
	# Get rid of #
	if(len(re.findall("#",line)) > 0):
		line = re.findall("^(.*)#",line)[0]
	# print(line)

	# Set strings
	for string_var in string_vars:
		k = re.findall("^ *{} *= *\"(.+)\"".format(string_var),line)
		if(len(k)>0):
			temp_string = k[0]
			print("set {} : {}".format(string_var,temp_string))
			exec("settings.{} = temp_string".format(string_var),globals())
			continue

	# Set ints
	for int_var in int_vars:
		k = re.findall("^ *{} *= *(.+)".format(int_var),line)
		if(len(k)>0):
			temp_int = int(k[0])
			print("set {} : {}".format(int_var,str(temp_int)))
			exec("settings.{} = temp_int".format(int_var),globals())

	# Set add_string_vars
	for add_string_var in add_string_vars:
		k = re.findall("^ *{}\.append\(\"(.+)\"\) *".format(add_string_var),line)
		if(len(k)>0):
			temp_string = k[0]
			print("append {} : {}".format(add_string_var,str(temp_string)))
			exec("settings.{}.append(temp_string)".format(add_string_var))

print("#####################################################")
print("Finished read settings by {}".format(settings_path))
print("#####################################################")


last_go_level_time = 0
last_go_infrastructure_time = 0
last_go_drone_time = 0
last_go_visit_friends_time = 0
last_go_collect_quests_time = 0
last_go_collect_mail_time = 0
last_go_shop_time = 0
last_go_hire_crew_time = 0
last_go_clue_time = 0
last_time = -1
work_cycle = -1

while(True):

	have_anything_to_do = False

	for a_work in settings.to_do_list:

		exec("last_time = last_{}_time".format(a_work))
		exec("work_cycle = settings.{}_cycle".format(a_work))

		print("ArknightsController: Check Work : {} ,last_time = {} , current_time = {} ,work_cycle = {}"
			.format(a_work, last_time, time.time(),work_cycle))

		if(last_time == 0 or time.time() - last_time > work_cycle):

			have_anything_to_do = True

			print("#####################################################")
			print("ArknightsController: Choose to do " + a_work + " ....")
			print("#####################################################")

			re = restart_app()

			if(re == "restart"):
				continue

			exec("last_{}_time = time.time()".format(a_work))

			exec("re = {}()".format(a_work))

			if(re == "restart"):
				continue

			print("#####################################################")
			print("ArknightsController: Finished " + a_work + " !")
			print("#####################################################")
			print("ArknightsController: Close the game")
			stop_app()

	if(have_anything_to_do == False):
		print("ArknightsController:No work to do yet.Sleep for "
			+ str(settings.recheck_time_when_no_work_to_do) +" seconds....")
		time.sleep(settings.recheck_time_when_no_work_to_do)
