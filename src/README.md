# Files

|       Path        | Description |
|-------------------|-------------|
| data              | Raw data scraped from [tagesschau.de](https://wetter.tagesschau.de/deutschland/wetterstationen/)
| averages          | Averaged temperature from ./data for each month.
| maps              | Generated Map files for [mapchart.net](https://mapchart.net/germany-districts.html)
| weatherscraper.py | Application to download data and save it in ``./data``
| webinterface.py   | API that downloads the data.
| schedule.py       | Waits for 14:00 System Time and then downloads the data.
| visualize.py      | Generated map files  from ``./averages``
| config.json       | Config file for visualize.py
