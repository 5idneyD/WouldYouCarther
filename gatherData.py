# import requests to 'get' page and bs4 to find relevant elements in html
import requests
from bs4 import BeautifulSoup as bs4
import json

# Using Auto Evolution data
url = "https://www.autoevolution.com/cars/"


page = requests.get(url)
soup = bs4(page.text, "html.parser")
# All the manufacturers names are stored in a span tag
makers = soup.find_all("span", {"itemprop": "name"})
# Remove the first 2 names as they are "Home" and "cars"
makers_names = [name.text for name in makers][2:]
# with open("cars.txt", "a") as f:
#     for i in makers_names:
#         name = i + "\n"
#         f.write(name)
# 




base_url = "https://www.autoevolution.com/"
final_data = {}

# Loop through the makers names, go to that makers own page, search for cars on that page
# for maker in makers_names:
# Convert the makers name to lower case and replace spaces with hyphens
# To follow the website's url syntax
for maker in makers_names:
    stripped_maker = maker.lower().strip().replace(" ", "-")
    maker_url = base_url + stripped_maker + "/"
    page = requests.get(maker_url)
    soup = bs4(page.text, "html.parser")
    models = soup.find_all("h4")
    models = [model.text for model in models]
    cars = []
    try:
        for model in models:
            model = model.replace(maker, "")[1:]
            cars.append(model)
    except TypeError as e:
        print("No models")

    print(stripped_maker, cars)
    final_data[stripped_maker] = cars



data = json.dumps(final_data)

with open("data.json", "w") as q:
    q.write(data)