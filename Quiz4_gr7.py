from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint


file = open('items.csv', 'w', encoding='utf-8_sig', newline='\n')
file_obj = csv.writer(file)
file_obj.writerow(['restaurant', 'address', 'locality', 'mobile number', 'categories'])

pagenum = 1
url = "https://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=Los%20Angeles%2C%20CA&page="
while pagenum <= 5:
    url = url + str(pagenum)
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")

    items = soup.find_all("div", {"class": "srp-listing clickable-area mdm"})
    if pagenum==3:
        print(r.text)
    for item in items:
        restaurant = item.span.text
        address = item.find("div", class_="street-address").text
        locality = item.find("div", class_="locality").text
        phonenum = item.find("div", class_='phones phone primary').text
        categories = item.find("div", class_='categories').find_all('a')
        categories = ", ".join([i.text for i in categories])
        file_obj.writerow([restaurant,address,locality,phonenum,categories])
    print(pagenum)
    pagenum += 1
    sleep(randint(15,20))

file.close()