from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

url = "https://pokemondb.net/pokedex/national"

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(req).read()

soup = BeautifulSoup(page, 'html.parser')

content = soup.find("div", class_="infocard-tall-list")
gen = 0
for item in content:
    if item.name == "h2":
        gen+=1
    elif item.name == "span":
        name = item.find("a", class_="ent-name").text
        number = item.find("small").text
        types = item.find("small", class_="aside").find_all("a")
        if len(types) == 2:
            type1 = types[0].text
            type2 = types[1].text
        else:
            type1 = types[0].text
            type2 = "NULL"

        print (name, number, gen, type1, type2)