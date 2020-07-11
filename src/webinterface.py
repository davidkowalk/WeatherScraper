from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup


def load(url):
    client = ureq(url)
    content = client.read()
    client.close()
    return content


def get_data():
    url = "https://wetter.tagesschau.de/deutschland/wetterstationen/"
    html = load(url)

    page_soup = soup(html, "html.parser")
    tables = page_soup.findAll("table")

    data = []

    for table in tables: #For each of the 4 tables
        rows = table.findAll("tr")  #Find all of the datapoints

        for row in rows: #For each of the datapoint in each row
            datapoint = []
            cells = row.findAll("td")

            cellcounter = 0

            for cell in cells: #Get each of the contents of the datapoint

                if cellcounter == 0:
                    content = cell.find("a").contents[0]
                elif cellcounter == 2:
                    content = cell.contents[0]
                    marker = content.find("°")
                    content = content[0:marker]
                elif cellcounter == 3:
                    content = cell.contents[0]
                    space = content.find(" ")
                    content = content[0:space]
                else:
                    content = cell.contents[0]

                cellcounter +=1
                datapoint.append(content) #Put the content in a custom datastructure

            if len(datapoint) > 0:
                data.append(datapoint)

    return data
