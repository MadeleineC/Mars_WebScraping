#coding: utf-8

# In[1]:


#import dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time


# In[2]:





# In[3]:


#Scrape the NASA Mars News Site and collect the latest News Title and Paragragh Text. 
#Assign the text to variables that you can reference later.

def nasa_scrape():
    browser = Browser('chrome', headless=False)

    nasa_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(nasa_url)

#Mars News
#scrape titles and news text for the first 3 pages
    nasa_dict_list = []


#click through 3 pages
# for x in range(3):
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    articles = soup.find_all('div', class_='list_text')

    for article in articles:
        date = article.find('div', class_='list_date').text
        title = article.find('div', class_='content_title').find('a').text
        p_text = article.find('div', class_='article_teaser_body').text
        
        dictionary = {"date":date, "title":title, "text":p_text}
        
        nasa_dict_list.append(dictionary)
        print(nasa_dict_list)
        
#     browser.click_link_by_partial_text('More')
    return nasa_dict_list


# nasa_scrape()

# In[4]:



        
    
    


# In[5]:


#Featured Mars Image
def jpl_scrape():
    browser = Browser('chrome', headless=False)

    jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jpl_url)

    # find the image url for the current Featured Mars Image 
    # and assign the url string to a variable called featured_image_url
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    article = soup.find("article", class_='carousel_item')
    style = article["style"]
    # print(style)
    image_str = style.split("'", 2)
    featured_image_url_part2 = image_str[1]

    jpl_url_split = jpl_url.split("/spaceimages", 1)
    featured_image_url_part1 = jpl_url_split[0]

    featured_image_url = featured_image_url_part1 + featured_image_url_part2

    print(featured_image_url)
    
    return featured_image_url


# In[6]:






# In[8]:


#Mars Weather
def mars_weather_scrape():
    browser = Browser('chrome', headless=False)

    twitter_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(twitter_url)

    time.sleep(30)
    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    mars_weather = soup.find("li", class_='stream-item').find("p", class_="tweet-text").text
    print(mars_weather)
    
    return mars_weather


# In[9]:





# In[10]:


#Mars Facts
def mars_facts_scrape():
    browser = Browser('chrome', headless=False)

    tables = pd.read_html("https://space-facts.com/mars/")
    print(len(tables))
    facts_table = tables[0]
    html_table = facts_table.to_html()
    return html_table


# In[11]:





# In[14]:


#Mars Hemispheres
def hemispheres_scrape():
    browser = Browser('chrome', headless=False)

    usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(usgs_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    hemispheres_dict_list = []
    links = browser.find_by_css(".itemLink h3")

    for i in range(len(links)):
        browser.find_by_css(".itemLink h3")[i].click()
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        image = soup.find("img", class_="wide-image")
        img_url = "https://astrogeology.usgs.gov" + image["src"]

        title = soup.find("h2", class_="title").text

        dictionary = {"title":title, "img_url":img_url}

        hemispheres_dict_list.append(dictionary)

        browser.back()
    print(hemispheres_dict_list)
    return hemispheres_dict_list


# In[15]:





# In[ ]:

def scrape():
    browser = Browser('chrome', headless=False)
    
    final_dictionary = {}
    
    nasa_dict_list = nasa_scrape()
    final_dictionary["nasa"] = nasa_dict_list
    
    featured_image_url = jpl_scrape()
    final_dictionary["jpl"] = featured_image_url
    
    mars_weather = mars_weather_scrape()
    final_dictionary["mars weather"] = mars_weather
    
    html_table = mars_facts_scrape()
    final_dictionary["mars facts"] = html_table
    
    hemispheres_dict_list = hemispheres_scrape()
    final_dictionary["hemisphere images"] = hemispheres_dict_list

    return final_dictionary

# scrape()

# print(final_dictionary)




