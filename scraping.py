import pandas as pd
import time
#from tqdm import tqdm_notebook as tqdm
#現在ではインポートの仕方が下のように変わっています
import tqdm
import raceid

def scrape_race_results(race_id_list):
    race_results = {}

    for race_id in race_id_list:
        time.sleep(1)
        try:
            url = "https://race.netkeiba.com/race/shutuba_past.html?race_id=" + race_id
            race_results[race_id] = pd.read_html(url)[0]
        except IndexError:
            continue
        #この部分は動画中に無いですが、捕捉できるエラーは拾った方が、エラーが出たときに分かりやすいです
        except Exception as e:
            print(e)
            break
        except:
            break
    return race_results

def syussou():
    race_id_list = raceid.get_id()
    #スクレイピングしてデータを保存
    test3 = scrape_race_results(race_id_list)
    for key in test3: #.keys()は無くても大丈夫です
        test3[key].index = [key] * len(test3[key])
    results = pd.concat([test3[key] for key in test3], sort=False) 
    return results
