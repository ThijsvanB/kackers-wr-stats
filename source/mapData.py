import shelve
import ast
import time

def get_all_saved_wrs():
    with shelve.open("wrs") as std:
        return list(std.keys())
    
def update_wr(number: int, fin: dict):
    with shelve.open("wrs", writeback=True) as std:
        std[number] = fin


def test_mapData(coreToken, liveToken, mapID = None):
    file = open("brokenmaps.txt")

    maps = file.readline().split("\\n")

    getRecordsUrl = "https://live-services.trackmania.nadeo.live/api/token/leaderboard/group/Personal_Best/map/{mapUid}/top?length=1&onlyWorld=true&offset=0"

    for i in range(len(maps)):
        urlReq = getRecordsUrl.replace("{mapUid}", maps[i])

        #x = requests.get(urlReq, headers={"Authorization": "nadeo_v1 t=" + liveToken})
        #print(x)
        #findata = ast.literal_eval(x.text)

        #fin = {}
        #fin["player"] = findata["tops"][0]["top"][0]["accountId"]
        #fin["score"] = findata["tops"][0]["top"][0]["score"]
        #fin["timestamp"] = findata["tops"][0]["top"][0]["timestamp"]

        #print(x, i + 1, fin)

        #update_wr(str(i + 1), fin)

        time.sleep(1)

def get_top_two(mapNr):
    ticket = get_ticket()
    liveToken = get_Live_API_token(ticket)  

    file = open("KRMapsIds.txt")
    maps = file.readline().split("\\n")

    getRecordsUrl = "https://live-services.trackmania.nadeo.live/api/token/leaderboard/group/Personal_Best/map/{mapUid}/top?length=2&onlyWorld=true&offset=0"

    urlReq = getRecordsUrl.replace("{mapUid}", maps[mapNr])

    x = requests.get(urlReq, headers={"Authorization": "nadeo_v1 t=" + liveToken[0]})
    print("Request records:", x)
    findata = ast.literal_eval(x.text)
    return [findata["tops"][0]["top"][0]["score"], findata["tops"][0]["top"][1]["score"]]