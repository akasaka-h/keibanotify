import scraping
import settings

def finder():
    race = scraping.syussou()
    # 教えてほしい馬settingsで決める
    race2 = race[race["馬名"].str.contains(settings.horse)]
    race_list = race2.index.to_list()
    house_num = race2["馬番"].to_list()
    course_list = []
    r_list = []
    res_list = []
    for race in race_list:
        course = race[4:6]
        if course == "01":
            course = "札幌"
        elif course == "02":
            course = "函館"
        elif course == "03":
            course = "福島"
        elif course == "04":
            course = "新潟"
        elif course == "05":
            course = "東京"
        elif course == "06":
            course = "中山"
        elif course == "07":
            course = "中京"
        elif course == "08":
            course = "京都"
        elif course == "09":
            course = "阪神"
        elif course == "10":
            course = "小倉"
        r = race[10:] + "R"
        course_list.append(course)
        r_list.append(r)
    for (course, r, num) in zip(course_list,r_list,house_num):
        res = str(course)+str(r)+"馬番:"+str(num)
        res_list.append(res)
    print(res_list)
    return res_list
