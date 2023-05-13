# import requests to 'get' page and bs4 to find relevant elements in html
import requests
from bs4 import BeautifulSoup as bs4
import json

# Using Auto Evolution data
url = "https://www.auto-data.net/en"


page = requests.get(url)
soup = bs4(page.text, "html.parser")
# All the manufacturers names are stored in a span tag
makers = soup.find_all("a", {"class": "marki_blok"})
# Remove the first 2 names as they are "Home" and "cars"
# makers_names = [name.text for name in makers][2:]
# with open("cars.txt", "a") as f:
#     for i in makers_names:
#         name = i + "\n"
#         f.write(name)
# 

data ={}
for m in makers:
    data[m.text] = m.get("href")


base_url = "https://www.auto-data.net/"
final_data = {}


for make, link in data.items():
    url = base_url + link
    print(make)
    page = requests.get(url)
    soup = bs4(page.text, "html.parser")
    divs = soup.find_all("a", {"class": "modeli"})
    models = []
    for div in divs:
        imgs = div.find_all("img")
        for i in imgs:
            if make in i.get("alt"):
                href = "https://www.auto-data.net/" + i.get("src")
                model = div.text.replace("\n", "")
                car = make + "?" + model
                final_data[car] = href

    #     models.append([div.text])
    # final_data[make] = models
    
print(final_data)

data = json.dumps(final_data)

with open("data.json", "w") as q:
    q.write(data)