# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import json


def main():
    config = get_config()
    stations = config["list"]

    for station in stations:
        coords = get_coordinates(station)

        config["positions"][station] = coords

    write_config(config)


def get_config():
    with open("config.json", "r", encoding="utf-8") as file:
        txt = file.read()

    return json.loads(txt)


def write_config(config):
    with open("config.json", "w", encoding="utf-8") as file:
        file.write(json.dumps(config, indent=4))


url = "https://wetter.tagesschau.de/deutschland/wetterstationen/"


def get_coordinates(station):
    # bs = station.encode("cp1252")
    # station = bs.decode("utf8")

    # station.decode('utf-8', 'ignore')
    station = station.replace("ä", "ae")
    station = station.replace("ü", "ue")
    station = station.replace("ö", "oe")
    station = station.replace("?", "ss")
    station = station.replace("-", "")

    if "/" in station:
        i = station.find("/") + 1
        station = station[i:]

    if " " in station:
        i = station.find(" ") + 1
        station = station[i:]

    print(f"sccraping {station}")

    content = requests.get(url + station.lower()).text
    soup = BeautifulSoup(content, "html.parser")

    try:
        lat = soup.find("meta", {"itemprop": "latitude"}).attrs["content"]
        lon = soup.find("meta", {"itemprop": "longitude"}).attrs["content"]
    except:
        lat = "ERROR"
        lon = "ERROR"

    return [lat, lon]


if __name__ == '__main__':
    main()
