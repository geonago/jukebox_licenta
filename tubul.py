from innertube import InnerTube
import sys
import json
from pytube import YouTube

PARAMS_TYPE_VIDEO = "EgIQAQ%3D%3D"
PARAMS_TYPE_CHANNEL = "EgIQAg%3D%3D"
PARAMS_TYPE_PLAYLIST = "EgIQAw%3D%3D"
PARAMS_TYPE_FILM = "EgIQBA%3D%3D"

client = InnerTube("WEB", "2.20230920.00.00")

data = client.search("arctic monkeys", params=PARAMS_TYPE_VIDEO)

items = data["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"][
    "sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"]

# id = items[0]["videoRenderer"]["videoId"]
id = "CQBOA061ugE"

path = "c:\\Users\\grig\\Desktop\\licentus\\The Conspiracy Theory Iceberg.mp"

def plm(ceva, byteceva, intceva):
    print(ceva)
    # print(byteceva)
    print(intceva)

def on_complete(ceva, intceva):
    print("DRACU")
    print(ceva)
    print(intceva)

plm = YouTube(f'https://youtu.be/{id}', on_progress_callback=plm, on_complete_callback=on_complete).streams.filter(res="360p", progressive="True").first().download()
# .download();
# for stream in streams:
#     print(stream)