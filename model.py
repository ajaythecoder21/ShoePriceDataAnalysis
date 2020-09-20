
# Import the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# import the dataset
df = pd.read_csv('Epic_Shoes.csv')

# Data Exploration and Cleaning
df.head()

# Data Analysis
df.drop('Unnamed: 0', axis = 1, inplace = True)
pd.set_option('display.max_rows', 200)
pd.set_option('display.max_columns', 200)

df.brand = df.brand.replace('Air Jordan Dub-Ze', 'Air Jordan')
df.brand = df.brand.replace('Air Jordan V (5)', 'Air Jordan')
df.brand = df.brand.replace('Nike Daybreak SPR', 'Nike')
df[25:].brand = df[25:].brand.replace('New Balance Women', 'New Balance')
df

df.brand = df.brand.replace('Saucony PEREGRINE', 'Saucony')
df.brand = df.brand.replace('Saucony Triumph I', 'Saucony')
df.brand = df.brand.replace('Saucony OmniRunni', 'Saucony')

df.brand.str.replace('Asics Gel Contend', 'Asics')
df.brand.str.replace('Asics Nitrofuze 2', 'Asics')

df.brand = df.brand.str.replace('Tretorn Nylite2pl', 'Tretorn')
df.brand = df.brand.str.replace('Tretorn Nylite17p', 'Tretorn')
df.brand = df.brand.str.replace('Tretorn Meg4Lifes', 'Tretorn')
df

df.brand = df.brand.where(-df.brand.str.startswith('Conv') == True, 'Converse' )
df.brand = df.brand.where(-df.brand.str.startswith('New') == True, 'New Balance')
df.brand = df.brand.where(-df.brand.str.startswith('Adi') == True, 'Adidas')
df.brand = df.brand.where(-df.brand.str.startswith('Asi') == True, 'Asics')
df.brand = df.brand.where(-df.brand.str.contains('Air Jor') == True, 'Air Jordan')
df.brand = df.brand.where(-df.brand.str.startswith('Nik') == True, 'Nike')
df

df.price = df.price.where(-df.price.str.startswith('8'), '84.99')
df
#df.price = df.price.replace('Shoes$1', np.NaN)
df.price = df.price.replace('l-Air Ki', np.NaN)
df.price = df.price.replace('Choose o', np.NaN)
df.price = df.price.replace('all Shoe', np.NaN)
df.price = df.price.replace('nning Sh', np.NaN)
df.price = df.price.replace('unning S', np.NaN)
df.price = df.price.replace('ng Shoes', np.NaN)
df.price = df.price.replace('unning S', np.NaN)
df.price = df.price.replace('g Shoes$', np.NaN)
df.price = df.price.replace('0\n\n\Choos', np.NaN)
df

df.dropna(axis = 0, inplace = True)
df

df.price = df.price.replace('$107.99\n', '107.99')
df.price = df.price.replace('es$111.9', '111.90')
df.price = df.price.replace('$170\n\nCh', '170')
df.price = df.price.replace('$84.99\n$', '84.99')
df.price = df.price.replace('es$68.99', '68.99')
df.price = df.price.replace('es$78.99', '78.99')
df.price = df.price.replace('73.99\n$9', '73.99')
df.price = df.price.replace('78.99\n$9', '78.99')
df.price = df.price.replace('65.99\n$9', '65.99')
df.price = df.price.replace('50.99\n$8', '50.99')
df.price = df.price.replace('.99\n$50\n', '50.00')
df.price = df.price.replace('9\n$130\n\n', '130')
df.price = df.price.replace('oes$91.9', '91.90')
df.price = df.price.replace('91.99\n$1', '91.99')
df.price = df.price.replace('0\n\nChoos', np.NaN)
df.price = df.price.replace('$49.99\n$', '49.99')
df
df.price = df.price.replace('65\n\nChoo', np.NaN)
df.price = df.price.replace('$78.99\n$', '78.99')
df.price = df.price.replace('$65.99\n$', '65.99')
df.price = df.price.replace('$124.99\n', '124.99')
df.price=df.price.replace('$39.99\n$', '39.99')
df.price = df.price.replace('154.99\n$', '154.99')
df.price = df.price.replace('99\n$25\n\n', '25.00')
df.price = df.price.replace('$124.99\n', '124.99')
df.price = df.price.replace('$99.99\n$', '99.99')
#df.price = df.price.replace('Shoes$1', np.NaN)
df.price = df.price.replace('$47.99\n$', '47.99')
df.price = df.price.replace('s$71.99\n', '71.99')
df.price =df.price.replace('es$55.99', '51.99')
df.price=df.price.replace('9\n$130\n\n', '130')
df.price = df.price.replace('Shoes$65', '65.00')
df.price = df.price.replace('99\n$130\n', '130')
#df.price = df.price.replace('Shoes$1', np.NaN)
df.price = df.price.replace('es$130.9', '130.90')
df
df.dropna(inplace = True, axis = 0)
#df.price = df.price.replace('Shoes$1', np.NaN)
df.drop(df.index[2], inplace = True, axis = 0)








