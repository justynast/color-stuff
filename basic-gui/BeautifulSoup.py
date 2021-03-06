""" tool to extract data from wikipedia list of colors """

from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

# specify the urls
quote_page = ['https://en.wikipedia.org/wiki/List_of_colors:_A%E2%80%93F',
              'https://en.wikipedia.org/wiki/List_of_colors:_G%E2%80%93M',
              'https://en.wikipedia.org/wiki/List_of_colors:_N%E2%80%93Z']

result = {} # dict storing final result

for pages in quote_page:

    # query the website and return the html to the variable ‘page’
    page = urlopen(pages)

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

    all_td = table.findAll('td')
    hex_cells = [] # table storig whole contet of td containing hex code

    for i in range(0, len(all_td)): # every ninth td stores hex code
        if i % 9 == 0:
            hex_cells.append(all_td[i])

    hex_names = []
    for hex in hex_cells: #extracs just hex codes and appends to a new list
        hex_code = hex.text
        hex_names.append(hex_code)

    color_dict = dict(zip(hex_names, color_names)) # make a dictionary with hex codes as keys and names as values
    result.update(color_dict) # merge with result dict

# save dictionary to json file
with open('color_dict.json', 'w') as f:
    json.dump(result, f)
