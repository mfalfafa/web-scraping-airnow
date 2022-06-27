import time
import requests
import os
import json

URL = "https://www.dosairnowdata.org/dos/AllPostsHistorical.json"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }

r = requests.get(URL, headers=HEADERS)
data = r.json()
cities = data.keys()

start_time = time.time()
for city in cities:
    print("city/state: %s" % city)
    d = data[city]["monitors"][0]["files"]
    for filename, fileurl in d.items():
        path_ = os.path.join(os.getcwd(), "historical-data\\" + city)
        # print(path)
        try:
            os.mkdir(path_)
        except:
            pass

        with open("{}\{}.csv".format(path_, filename), "wb") as f:
            r = requests.get(fileurl, headers=HEADERS)
            f.write(r.content)
            print("writing: %s.csv \t into %s" % (filename, "/historical-data/" + city))
    print()
        # print(filename)
        # print(fileurl)
        # break
    # break

with open("AllPostsHistorical.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("finished in %s.3f" % (time.time()-start_time))
print("all historical data can be seen at 'historical-data' folder.")
