from webinterface import get_data
from pandas import DataFrame
from datetime import date
from datetime import datetime

def main():
    data = get_data()

    data_frame = DataFrame(data)

    time = datetime.now()

    current_date = str(date.today())
    current_hour = str(time.hour)
    current_minute = str(time.minute)

    data_frame.to_csv(f"./data/{current_date}-{current_hour}-{current_minute}.csv", header=["Station", "Wetter", "Temperatur", "Windgeschwindigkeit"], index = False, encoding = 'utf8')

    print(f"Created {current_date}-{current_hour}-{current_minute}.csv")



if __name__ == '__main__':
    main()
