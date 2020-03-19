from webinterface import get_data
from pandas import DataFrame
from datetime import date

def main():
    data = get_data()

    data_frame = DataFrame(data)

    current_date = str(date.today())

    data_frame.to_csv(f"./data/{current_date}.csv", header=["Station", "Wetter", "Temperatur", "Windgeschwindigkeit"], index = False, encoding = 'utf8')



if __name__ == '__main__':
    main()
