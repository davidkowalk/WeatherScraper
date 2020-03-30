from pandas import read_csv
from pandas import read_csv
from pandas import DataFrame

def main():
    file_names = [
        "2020-03-19-13-40.csv",
        "2020-03-20-13-41.csv",
        "2020-03-21-13-22.csv",
        "2020-03-22-17-15.csv",
        "2020-03-23-17-4.csv",
        "2020-03-24-15-51.csv",
        "2020-03-25-14-5.csv",
        "2020-03-25-14-10.csv",
        "2020-03-26-15-37.csv",
        "2020-03-27-14-11.csv",
        "2020-03-28-14-4.csv",
        "2020-03-29-14-2.csv",
        "2020-03-30-15-11.csv"
    ]

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

    avg_temp.to_csv("./averages/march.csv", index=False)


if __name__ == '__main__':
    main()
