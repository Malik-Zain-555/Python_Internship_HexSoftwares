import requests
from bs4 import BeautifulSoup
import csv

with open ("book.csv","w",newline="",encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title","Price","Star Rating"])

        for i in range(1,51):
            url = f"https://books.toscrape.com/catalogue/page-{i}.html"

            response = requests.get(url=url)

            actualHtmlFormat = response.text

            soup = BeautifulSoup(actualHtmlFormat, "html.parser")

            books = soup.find_all("article")        
            
            for book in books:
                title = book.h3.a["title"]
                price = book.find("p", class_="price_color").text.replace("Â£","£")
                starRating = book.find("p",class_="star-rating")["class"][1]
                
                writer.writerow([title,price,starRating])