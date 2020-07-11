from datetime import datetime
from time import sleep
from weatherscraper import main as scrape


def main():
    print("Scheduling Scan")
    repeat = True

    while repeat:
        time = datetime.now()
        current_hour = time.hour

        if current_hour >= 14:
            try:
                scrape()
                repeat = False
                print("Done")
            except:
                print("Failed")
        else:
            sleep(5 * 60)  # Check every five minutes


if __name__ == '__main__':
    main()
