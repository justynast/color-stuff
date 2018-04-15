""" tool to extract data from wikipedia list of colors """

from urllib.request import urlopen
from bs4 import BeautifulSoup

# specify the url
quote_page = 'https://en.wikipedia.org/wiki/List_of_colors:_A%E2%80%93F'

# query the website and return the html to the variable ‘page’
page = urlopen(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# find the table
table = soup.find('table', {'class':'wikitable sortable'})

# create a table to store html of links including color names
color_links = []

for th in table.findAll('th'): # find all header cells and append to a list
    color_links.append(th)

del color_links[:10] # delete unnecessary ones

# table to store names
color_names = []

for color in color_links: # extract just names of the colors and append to a list
    color_name = color.text
    color_names.append(color_name)

print(color_names)
