import json

TIME = "109-1"

f = open(f"NTU {TIME}.json", 'r', encoding="utf8")
ntu_courses = json.loads(f.read())["List"]
f.close()

f = open(f"NTUST {TIME}.json", 'r', encoding="utf8")
ntust_courses = json.loads(f.read())["List"]
f.close()

f = open(f"NTNU {TIME}.json", 'r', encoding="utf8")
ntnu_courses = json.loads(f.read())["List"]
f.close()

'''
for key in ntnu_courses[0].keys():
    print("    del", "course[\"" + str(key) + "\"]")
'''

'''
count = 0
for course in ntu_courses:
    count += 1
for course in ntust_courses:
    count += 1
for course in ntnu_courses:
    count += 1
print(count)
'''

for course in ntnu_courses:
    del course["applyCode"]
    del course["summerPhase"]

all_courses_list = []
all_courses_list.extend(ntu_courses)
all_courses_list.extend(ntust_courses)
all_courses_list.extend(ntnu_courses)

for course in all_courses_list:
    del course["acadmTerm"]
    del course["acadmYear"]
    # del course["applyCode"]
    del course["authorizeP"]
    # del course["chnName"]
    del course["class1"]
    # del course["courseCode"]
    del course["courseGroup"]
    del course["courseKind"]
    # del course["credit"]
    # del course["deptCode"]
    del course["deptGroup"]
    del course["domain"]
    del course["engName"]
    del course["engTeach"]
    del course["formS"]
    del course["insDeptCode"]
    del course["limitCountH"]
    del course["moocs"]
    # del course["optionCode"]
    # del course["serialNo"]
    del course["sex_restrict"]
    # del course["summerPhase"]
    # del course["teacher"]
    # del course["timeInfo"]
    course["vChnName"] = course.pop("v_chn_name")    # del course["v_chn_name"]
    del course["v_class1"]
    course["vComment"] = course.pop("v_comment")    # del course["v_comment"]
    course["vDeptChiabbr"] = course.pop("v_deptChiabbr")    # del course["v_deptChiabbr"]
    del course["v_deptGroup"]
    del course["v_error"]
    del course["v_is_Full"]
    course["vLimitCourse"] = course.pop("v_limitCourse")    # del course["v_limitCourse"]
    del course["v_phase"]
    del course["v_priority"]
    del course["v_release_time"]
    del course["v_reserve_count"]
    del course["v_stage"]
    del course["v_stfseld"]
    del course["v_stfseld_auth"]
    del course["v_stfseld_deal"]
    del course["v_stfseld_exchange"]
    del course["v_stfseld_undeal"]
    del course["v_stfseld_unfull"]

f = open(f"public_course ({TIME}).json", 'w', encoding="utf-8")
all_courses_json = json.dumps(all_courses_list, indent = 4, ensure_ascii=False)
f.write(all_courses_json)
f.close()