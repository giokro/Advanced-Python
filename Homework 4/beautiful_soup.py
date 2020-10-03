from bs4 import BeautifulSoup
from requests_html import HTMLSession
import requests
import json

products = []

# this is for getting the products added by javascript
session = HTMLSession()
resp = session.get("https://www.osta.ee/en/category/computers")
resp.html.render() # run the site's javascript

soup = BeautifulSoup(resp.html.html, "lxml") # "lxml" is the parser we use for the site

owl_items = soup.find_all("div", class_="owl-item") # these are special offer items added by js
for item in owl_items:
	title = item.find("p")["title"]
	price = item.find("span", class_="discount-price").text.replace("\u20ac", " euro")
	img = item.find("img")["src"]

	products.append({"Title": title, "Price": price, "Picture href": img})
	print("product scraped:", title)

totalPages = int(soup.find("span", class_="totalPageCount").text)

# for getting all products from all pages
for i in range(totalPages):
	link = "https://www.osta.ee/en/category/computers/page-"+str(i+1) # move through the pages
	tSite = requests.get(link).text
	soup = BeautifulSoup(tSite, "lxml")
	
	productList = soup.find_all("li", class_="mb-30")
	
	for product in productList:
		title = product.find("p", class_="offer-thumb__title").text.replace("\n", "") # removes leftover "\n"-s
		price = product.find("span", class_="price-cp").text.replace("\u20ac", " euro") # replace euro sign with euro
		img = product.find("img")["data-original"]

		products.append({"Title": title, "Price": price, "Picture href": img})
		print(f"{i+1}/{totalPages} scraped:", title)


with open("products.json", "w") as json_file: # write the data in a json file
	json.dump(products, json_file)

print(products)
print("total products:", len(products))







	


	
