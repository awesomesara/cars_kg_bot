import requests
from bs4 import BeautifulSoup
import json

def get_html(url):
    response = requests.get(url) 
    # print(response.status_code)
    return response.text


def write_to_json(data):
    with open('carskg.json','w') as file:
        json.dump(data,file,ensure_ascii=False, indent=2)
        

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    product_list = soup.find('div', class_="main catalog").find('div', class_='catalog-list')
    products = product_list.find_all('a', class_='catalog-list-item')
     
    list_ = []

    for product in products:
        #img title price descr

        try:
            title = product.find('span', class_="catalog-item-params").find('span', class_='catalog-item-caption').text.strip()
            
        except:
            title = ''
        try:
            img = product.find('img').get('src')
            
        except:
            img = ''
        try:
            price = product.find('span', class_="catalog-item-price").text
            
        except:
            price = ''
        try:
            descr = product.find('span', class_="catalog-item-descr").text.strip()
            
        except:
            descr = ''

        data = {'title': title, 'img': img, 'descr': descr, 'price': price}
        list_.append(data)
    write_to_json(list_)



def main():
    cars_url = 'https://cars.kg/offers'
    # pages = '?page='

    
    get_page_data(get_html(cars_url))
    
 
main()
