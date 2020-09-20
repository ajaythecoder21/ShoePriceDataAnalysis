# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 20:23:32 2020

@author: Rithi
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
uc = requests.get(
    'https://www.sneakerhead.com/collections/shoes')

soup = BeautifulSoup(uc.content, 'html.parser')

product = soup.find(class_ = 'product-list product-list--collection product-list--with-sidebar')

brand = [product.div.get_text()[7:17]]
brand

price = [product.div.get_text()[42:49]]
price

gender = [np.NaN]
gender

second_product = [it.get_text() for it in product]
brand_name = []
prices = []
for i in second_product:
    brand_name.append(i[7:24])
    prices.append(i[42:50])
brand_name
prices

shoes = pd.DataFrame(
    {
    'brand': brand_name,
    'price': prices,
   } )

shoes.to_csv('Epic_Shoes.csv')

