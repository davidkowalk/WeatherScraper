from pandas import read_csv
from pandas import read_csv
from pandas import DataFrame
from json import loads

def main():

    month = "april"

    file_names = get_files()[month]

    files = []

    # Load all Files into Datastructure
    for name in file_names:
        files.append(read_csv("./data/"+name))

    # Initialize Average temperature file
    avg_temp = DataFrame(columns = ["Station", "Temperatur"])


    # Load The first file into DataFrame
    first = files[0]

    for i, row in first.iterrows():
        avg_temp.loc[i] = [row["Station"], row["Temperatur"]]


    #Add all succeeding files
    for file in files[1:]:
        for i, row in file.iterrows():
            avg_temp.at[i, "Temperatur"] += row["Temperatur"]


    # Divide all tempereatures by the number of summs to get average
    length = len(file_names)

    for i in range(len(avg_temp)):
        avg_temp.at[i, "Temperatur"] /= length

    avg_temp.to_csv(f"./averages/{month}.csv", index=False)


def get_files():
    return loads(open("./data/files.json").read())


if __name__ == '__main__':
    main()
