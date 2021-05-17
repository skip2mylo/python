"""
BI20 PYTHON
Inlämningsuppgift 3
by Yijun Cao
"""
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

#read the source file
df = pd.read_excel('books.xlsx')

"""
df.info()
#Inspect the dataset

"""
#drop unneeded columns
df = df.drop(columns=['Edition Statement',
                                    'Contributors',
                                    'Corporate Author',
                                    'Corporate Contributors',
                                    'Publisher',
                                    'Former owner',
                                    'Engraver',
                                    'Contributors',
                                    'Issuance type',
                                    'Flickr URL',
                                    'Shelfmarks'])

#set an index
df.set_index('Identifier', inplace=True)

#handle NaN
df['Author'].fillna('Unknown', inplace=True)

"""
clean 'Date of Publictaion'
extract first 4 digits by calling regex

"""
#inspect the data first
#df['Date of Publication'].value_counts().head(50)

df['Date of Publication'] = df['Date of Publication'].str.extract(r'(\d{4})', expand=False)
df['Date of Publication'] = pd.to_numeric(df['Date of Publication'])
#check how it looks after cleansing
#df['Date of Publication'].head(10)


"""
clean 'Place of Publictaion'
extract Boston, London, Oxford (three of most found cities) from messy string
use np array condition

"""
#inspect the data first
#df['Place of Publication'].value_counts().head(50)

Boston = df['Place of Publication'].str.contains('Boston')
London = df['Place of Publication'].str.contains('London')
Oxford = df['Place of Publication'].str.contains('Oxford')
df['Place of Publication'] = np.where(Oxford,'Oxford',
                                np.where(Boston,'Boston',
                                    np.where(London,'London',
                                        df['Place of Publication'].str.replace('-',' '))))
#check how it looks after cleansing
#df['Place of Publication'].head(10)

"""
clean 'Author'
set all value in lower cases
trim redundent characters for 'tennyson, alfred'(the author appears twice on the list of Top 50)
drop all values followed by '-'(usually a title or redundent characters)

"""
#inspect the data first
df['Author'] = df['Author'].str.lower()
#df['Author'].value_counts().head(50)

df['Author'] = np.where(df['Author'].str.contains('tennyson, alfred'),'tennyson, alfred',df['Author'].str.replace(r'(-.*)',''))
#check how it looks after cleansing
#df['Author'].head(10)

df.to_excel('books_3.xlsx',sheet_name='books_clean')

"""
Graph function

"""


def over_year():
    fig= plt.figure(figsize=(10,4))
    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    axes.set_xlabel('Year')
    axes.set_ylabel('Number of Publications')
    axes.set_title('Number of Books Published over Years ')
    bin = np.arange(1500,1950,10)
    axes.hist(df['Date of Publication'],bins=bin)
    plt.show()

def author_books():
    df['Author'].value_counts().head(10).plot.barh()
    plt.xlabel("Number of books")
    plt.ylabel("Authors")
    plt.title("Top 10 authors wrote the most books")
    plt.show()

def city_books():
    df['Place of Publication'].value_counts().head(10).plot.bar()
    plt.xlabel("Place of Publications")
    plt.ylabel("Number of books published")
    plt.title("Top 10 cities published the most books")
    plt.show()

while True:
    print('Select the number of graphs you want to see: \n')
    print('1. Books published over years')
    print('2. Top 10 authors that wrote the most books')
    print('3. Top 10 cities that published most books')
    print('4. Exit ')

    num = int(input('Plase input the number: '))
    lis = [1,2,3,4]

    if num not in lis:
        print('The number you input is not valid.\n')
    elif num ==1:
        over_year()
    elif num ==2:
        author_books()
    elif num ==3:
        city_books()
    elif num ==4:
        break



    