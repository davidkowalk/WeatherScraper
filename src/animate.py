import json
from visualize import generate_vis
from pandas import read_csv

def main():
    sorted_index = load_index()["averages"]
    config = get_config()

    data_cube = []

    print("Reading data...")

    for path in sorted_index:
        data_cube.append(read_csv("averages/"+path))

    extremes = get_extremes(data_cube, config)

    print("Extremes:", extremes)
    print("Generating Frames...")
    frames = generate_frames(extremes, data_cube, config)

    print("\nSaving to disk...")
    i = 0
    for frame in frames:
        with open(f"./animation/frame_{i}.txt", "w", encoding = "utf8") as file:
            json.dump(frame, file)

        i += 1

def generate_frames(extremes, data_cube, config):

    frames = []

    min_temp = extremes[0]
    max_temp = extremes[1]

    for sheet in data_cube:
        frames.append(generate_vis(config["stations"], sheet, min_temp, max_temp))


    return frames

def get_extremes(data_cube, config):

    lowest = data_cube[0].at[0, "Temperatur"]
    highest = data_cube[0].at[0, "Temperatur"]

    for sheet in data_cube:
        for i, row in sheet.iterrows():

            if row["Station"] in config["ignore"]:
                continue

            if row["Temperatur"] < lowest:
                lowest = row["Temperatur"]
            elif row["Temperatur"] > highest:
                highest = row["Temperatur"]

    return (lowest, highest)


def load_index():
    index = "averages/averages.json"

    with open(index) as file:
        txt = file.read()

    return json.loads(txt)



def get_config():
    with open("./config.json",encoding='utf8') as file:
        config = json.load(file)
    return config



if __name__ == '__main__':
    main()
