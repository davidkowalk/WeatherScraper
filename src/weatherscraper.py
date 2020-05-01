from webinterface import get_data
from pandas import DataFrame
from datetime import date
from datetime import datetime
import json

index_file = "data/files.json"
month = "may"

def main():
    data = get_data()

    data_frame = DataFrame(data)

    time = datetime.now()

    current_date = str(date.today())
    current_hour = str(time.hour)
    current_minute = str(time.minute)

    data_frame.to_csv(f"./data/{current_date}-{current_hour}-{current_minute}.csv", header=["Station", "Wetter", "Temperatur", "Windgeschwindigkeit"], index = False, encoding = 'utf8')

    fname = f"{current_date}-{current_hour}-{current_minute}.csv"

    print(f"Created {fname}")

    update_index(month, fname)

def update_index(month: str, name: str):
    index = read_index()

    if month not in index:
        index[month] = []

    index[month].append(name)

    write_index(index)


def read_index():
    with open(index_file) as index:
        txt = index.read()

    return json.loads(txt)

def write_index(index):
    with open(index_file, "w") as file:
        file.write(json.dumps(index, indent=4))

if __name__ == '__main__':
    main()
