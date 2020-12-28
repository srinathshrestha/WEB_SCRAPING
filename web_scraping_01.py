'''
there are 2 ways of web scraping:
1 .  through API
2 .  through HTML by BS4,etc '''

import requests
from bs4 import BeautifulSoup

url = "http://codewithharry.com"
# getting the HTML
r = requests.get(url)
html_content = r.content

# parsing the html
suop = BeautifulSoup(html_content,'html.parser')
# print(suop.prettify)

# html tree traversal
tittle =  suop.title
# print(tittle)

# getting all the paras in html page
paras =suop.find_all('p')
# print(paras)

# getting all the ancher tags in html page
ancher_tag =suop.find_all('a')
# print(ancher_tag)

# geting 1st ellemenst in htm
a = suop.find('p')
# print(a)

# get class of any ellements
b = suop.find_all('p',['class']) # find will give the 1st and find_all will give all ellements
# print(b)

# get all the ellements with lead class
c = suop.find_all('p',class_ ='lead')
# print(c)

# get the text from all tags?suop
d = suop.find('p').get_text()
# print(d)
e = suop.get_text
# print(e)

# getting all the links in the html
all_link = set()
for link in ancher_tag :
    if (link.get('href') != "#"):
        link = 'http://codewithharry.com'+link.get('href')
        # all_link.add(link)
        # print(link)

#.contents - a tag's children are available as a list. all our elements will be stored in a memory
#.children - a tag's children are available as a generator.  . won't store in memory. but can be itrrable
navbarsupportedcontent = suop.find(id ='navbarSupportedContent' )
# for ele in navbarsupportedcontent.children:
    # print(ele)

navbarsupportedcontent = suop.find(id ='navbarSupportedContent' )
# for ele in navbarsupportedcontent.contents:
    # print(ele)


#for item in navbarsupportedcontent.stripped_strings:
#   print(item)


# printing the parents tags of any ellements
# print(navbarsupportedcontent.parent)
# print(navbarsupportedcontent.parents)
# print(navbarsupportedcontent.previous_sibling.previous_sibling)
e = suop.select('#loginModal')
print(e)