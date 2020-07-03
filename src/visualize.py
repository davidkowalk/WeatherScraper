import json
from pandas import read_csv
import colorsys

def main():

    global config

    path = input("Path: ")
    config = get_config()
    station_mapping = config["stations"]

    data = read_csv(path)

    min_temp, max_temp = get_extremes(data)
    print(min_temp, max_temp)

    vis = generate_vis(station_mapping, data, min_temp, max_temp)


    with open("./maps/map.txt", "w", encoding="utf8") as file:
        json.dump(vis, file)

def get_config():
    with open("./config.json",encoding='utf8') as file:
        config = json.load(file)
    return config


def generate_vis(station_mapping, data, min_temp, max_temp): #Generate the configuartion-file for mapchart.net
    vis = {
        "title":"Temperature in Germany",
        "hidden":[],
        "background":"#21252B",
        "borders":"#ffffff"
    }

    groups = {}

    for i in range(len(data["Station"])):

        station = data["Station"][i] # Get the station at pos i
        maps = station_mapping[station] # Get Landkreise

        #Generate Color
        temperature = data["Temperatur"][i]
        hue = map_hue(min_temp, max_temp, temperature)
        saturation = 71
        value = 72

        color = hsv_to_hex(hue, saturation, value)


        #Generate Group with Color -> Set div and path
        if color in groups:
            group = groups[color]
            group["label"] += ", "+station

            for map in maps:
                group["paths"].append(map)
        else:
            groups[color] = {
                "div":f"#box{i}",
                "label":station,
                "paths":maps
                }

    vis["groups"] = groups

    return vis


def get_extremes(data):
    lowest = data.at[0, "Temperatur"]
    highest = data.at[0, "Temperatur"]

    for i, row in data.iterrows():

        if row["Station"] in config["ignore"]:
            continue

        if row["Temperatur"] < lowest:
            lowest = row["Temperatur"]
        elif row["Temperatur"] > highest:
            highest = row["Temperatur"]

    return (lowest, highest)


def map_hue(min, max, x):
    space = 200
    return -(space*x)/(max-min)+(space*max)/(max-min)


def hsv_to_hex(h,s,v):
    rgb = tuple(int(round(i * 255)) for i in colorsys.hsv_to_rgb(h/360,s/100,v/100))
    print(rgb)
    return '#%02x%02x%02x' % rgb


if __name__ == '__main__':
    main()
