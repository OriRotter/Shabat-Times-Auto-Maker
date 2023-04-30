from PIL import Image, ImageFont, ImageDraw
import requests


fontT = ImageFont.truetype("title.ttf", 35)
fontNum = ImageFont.truetype("number.ttf", 30)

year = input("Enter a year: ")
r = requests.get(f"https://data.gov.il/api/3/action/datastore_search?resource_id=cfe1dd76-a7f8-453a-aa42-88e5db30d567&q={year}")
data = r.json()
for shabat in data["result"]["records"]:
    my_image = Image.open("shabat.png")
    image_editable = ImageDraw.Draw(my_image)
    print(shabat)

    title = shabat["parasha"][::-1]

    jsTimeIn = str(shabat["Jerusalem_in"])
    jsTimeIn = jsTimeIn[:len(jsTimeIn)-3]

    jsTimeOut = str(shabat["Jerusalem_out"])
    jsTimeOut = jsTimeOut[:len(jsTimeOut) - 3]

    telAvivTimeIn = str(shabat["TelAviv_in"])
    telAvivTimeIn = telAvivTimeIn[:len(telAvivTimeIn)-3]

    telAvivTimeOut = str(shabat["TelAviv_out"])
    telAvivTimeOut = telAvivTimeOut[:len(telAvivTimeOut) - 3]

    hayfaTimeIn = str(shabat["Hayfa_in"])
    hayfaTimeIn = hayfaTimeIn[:len(hayfaTimeIn)-3]

    hayfaTimeOut = str(shabat["Hayfa_out"])
    hayfaTimeOut = hayfaTimeOut[:len(hayfaTimeOut) - 3]

    beerShevaTimeIn = str(shabat["BeerSheva_in"])
    beerShevaTimeIn = beerShevaTimeIn[:len(beerShevaTimeIn) - 3]

    beerShevaTimeOut = str(shabat["BeerSheva_out"])
    beerShevaTimeOut = beerShevaTimeOut[:len(beerShevaTimeOut) - 3]

    w = image_editable.textlength(title,font=fontT)
    image_editable.text((135-((w-50)//2), 93), title, "red", font=fontT)

    image_editable.text((183,245), jsTimeIn, "red", font=fontNum)
    image_editable.text((113, 245), jsTimeOut, "red", font=fontNum)

    image_editable.text((183,280), telAvivTimeIn, "red", font=fontNum)
    image_editable.text((113, 280), telAvivTimeOut, "red", font=fontNum)

    image_editable.text((183,315), hayfaTimeIn, "red", font=fontNum)
    image_editable.text((113, 315), hayfaTimeOut, "red", font=fontNum)

    image_editable.text((183,353), beerShevaTimeIn, "red", font=fontNum)
    image_editable.text((113, 353), beerShevaTimeOut, "red", font=fontNum)
    my_image.save(f'output/{title[::-1]}.png', 'png')

