try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
#import the library used to query a website

from bs4 import BeautifulSoup
# specify the url
quote_page = 'https://www.target.com/c/slow-cookers-roasters-kitchen-appliances-dining/-/N-5xtrg'

# query the website and return the html to the variable 'page'
page = urllib2.urlopen(quote_page)

# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of name and get its value
name_box = soup.find('div', attrs={'class': 'truncated-title'})

name = name_box.text.strip() # strip() is used to remove starting and trailing
print (name)

# get the index price
price_box = soup.find('div', attrs={'class':'price'})
price = price_box.text
print (price)
