######################### 由 settings.txt 控制的配置 ###########################################

adb_path = ""
device_address = ""
to_do_list = []
auto_t_level = []
auto_ce_level = 5
auto_ls_level = 5
go_level_cycle = 10800
go_infrastructure_cycle = 21600
go_visit_friends_cycle = 21600
go_collect_quests_cycle = 7200
go_collect_mail_cycle = 21600
go_shop_cycle = 21600
go_hire_crew_cycle = 10800
go_clue_cycle = 21600
go_drone_cycle = 7200
recheck_time_when_no_work_to_do = 3600



######################### 不由 settings.txt 控制的配置 ###########################################

# 公开招募时遇见以下词条则停止自动公开招募
go_hire_stop_options = ["高级资深干员","资深干员"]

screenshot_path = r"temp_screenshot\screenshot.png"

last_screenshot_path = r"temp_screenshot\last_screenshot.png"

except_dist = 5

package_name = "com.hypergryph.arknights"

accidents = {
			"paths":[r"template_images\accident_activities.png",
					r"template_images\accident_daily_gift.png",
					r"template_images\accident_data_refreash.png",
					r"template_images\accident_level_up.png",
					r"template_images\accident_monthly_check_in.png",
					r"template_images\accident_no_cp.png",
					r"template_images\accident_no_cp_2.png",
					r"template_images\accident_shop_tip1.png",
					r"template_images\accident_gift2.png"
					],
			"thresholds":[0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05],
			"methods":["click","click","restart","click","click","restart","restart","click","click"],
			"click_offset":[None,None,None,None,None,None,None,(0,-100),None]
			}