#!/usr/bin/env python
# coding: utf-8

# In[1]:


# dependecies and modules
from bs4 import BeautifulSoup as bs
from splinter import Browser
from urllib.parse import urlsplit
import pandas as pd
import os
import time


# In[2]:


executable_path = {"executable_path":"C:\webdrivers\chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless = False)


# In[3]:


# Mars News


# In[4]:


url = "https://mars.nasa.gov/news/"
browser.visit(url)


# In[5]:


html = browser.html
soup = bs(html, "html.parser")


# In[6]:


news_title = soup.find("div",class_="content_title").text
news_paragraph = soup.find("div", class_="article_teaser_body").text
print(f"Title: {news_title}")
print(f"Para: {news_paragraph}")


# In[7]:


# JPL Mars Space Images


# In[8]:


url_image = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url_image)


# In[9]:


from urllib.parse import urlsplit
base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(url_image))
print(base_url)


# In[10]:


xpath = "//*[@id=\"page\"]/section[3]/div/ul/li[1]/a/div/div[2]/img"


# In[11]:


results = browser.find_by_xpath(xpath)
img = results[0]
img.click()


# In[12]:


html_image = browser.html
soup = bs(html_image, "html.parser")
img_url = soup.find("img", class_="fancybox-image")["src"]
full_img_url = base_url + img_url
print(full_img_url)


# In[13]:


# Mars Weather


# In[14]:


url_weather = "https://twitter.com/marswxreport?lang=en"
browser.visit(url_weather)


# In[15]:


html_weather = browser.html
soup = bs(html_weather, "html.parser")
#temp = soup.find('div', attrs={"class": "tweet", "data-name": "Mars Weather"})
mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
print(mars_weather)


# In[16]:


# Mars Facts


# In[17]:


url_facts = "https://space-facts.com/mars/"


# In[18]:


table = pd.read_html(url_facts)
table[0]


# In[19]:


df_mars_facts = table[0]
df_mars_facts.columns = ["Parameter", "Values"]
df_mars_facts.set_index(["Parameter"])


# In[20]:



mars_html_table = df_mars_facts.to_html()
mars_html_table = mars_html_table.replace("\n", "")
mars_html_table


# In[21]:


# Mars Hemispheres


# In[42]:


url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url)


# In[43]:


hemisphere_image_urls = []

# Get a List of All the Hemispheres
links = browser.find_by_css("a.product-item h3")
for item in range(len(links)):
    hemisphere = {}
    
    # Find Element on Each Loop to Avoid a Stale Element Exception
    browser.find_by_css("a.product-item h3")[item].click()
    
    # Find Sample Image Anchor Tag & Extract <href>
    sample_element = browser.find_link_by_text("Sample").first
    hemisphere["img_url"] = sample_element["href"]
    
    # Get Hemisphere Title
    hemisphere["title"] = browser.find_by_css("h2.title").text
    
    # Append Hemisphere Object to List
    hemisphere_image_urls.append(hemisphere)
    
    # Navigate Backwards
    browser.back()


# In[44]:


hemisphere_image_urls


# In[ ]:




