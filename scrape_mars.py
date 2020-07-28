#The following code scrapes various websites for data related to the Mission to Mars

# Dependencies
import pandas as pd
from bs4 import BeautifulSoup
from splinter import Browser
import requests
import re
import time

def scrape():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    #Nasa Mars Latest News-------------------------------------------------------------------------------------------------
    i=1
    while (not i>=3):
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
        browser.visit(url)
        if soup.find('div', class_="list_text"):
            news_title=soup.find('div', class_="list_text")
            news_title=news_title.find('div', class_='content_title').text
            news_p=soup.find('div', class_="article_teaser_body").text
            break
        else:
            i+=1
            time.sleep(3)
    
    #JPL Mars Space Images - Featured Image---------------------------------------------------------------------------------
    #Visit NASA Images Website
    jpl_url="https://www.jpl.nasa.gov"
    image_url="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)
    #Scrape NASA Website for featured image
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    featured_image=browser.find_by_id('full_image')['data-fancybox-href']
    featured_image_url=jpl_url+featured_image
    

    #Mars Weather ---------------------------------------------------------------------------------------------------------
    #Visit Mars Weather Twitter Account and wait for the page to load
    weather_html = browser.html
    soup = BeautifulSoup(weather_html, 'html.parser')
    weather_url="https://twitter.com/marswxreport?lang=en"
    browser.visit(weather_url)
    time.sleep(3)
    # # Visit Mars Weather Twitter Account
    i=1
    while i<5:
        try:
            weather_html = browser.html
            soup = BeautifulSoup(weather_html, 'html.parser')
            weather_url="https://twitter.com/marswxreport?lang=en"
            browser.visit(weather_url)
            mars_weather=str(soup.find_all(text=re.compile("InSight"))[0])
            break
        except:
            i=i+1
            continue


    #Mars Facts ---------------------------------------------------------------------------------------------------------
    #Visit Mars Facts webpage
    mars_facts_url="https://space-facts.com/mars/"
    #Scrape Mars Facts Website for table containing facts
    table=pd.read_html(mars_facts_url)
    facts=table[0]
    facts.columns=('Property','Value')
    facts=facts.set_index('Property')
    #Convert to html
    table_html=facts.to_html(classes="table table-striped table-borderless", justify="left")
    #facts.to_html(open('Output/mars_facts_table.html', 'w'))

    #Mars Hemispheres -----------------------------------------------------------------------------------------------------
    #Visit the USGS Astrogeology site
    short_url="https://astrogeology.usgs.gov/"
    usgs_url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(usgs_url)
    #Obtain high resolution images for each of the Mars Hemispheres
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    hemispheres=soup.find_all('div', class_="item")
    hemispheres

    #Create dictionnary to store data
    hemisphere_image_urls=[]

    # Loop thru the hemispheres
    for hemisphere in hemispheres:
        title=hemisphere.find('h3').text
        title=title.replace("Enhanced","")
        image_relative_url=hemisphere.find('a')['href']
        hemisphere_url=short_url+image_relative_url
        browser.visit(hemisphere_url)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        results=soup.find('div', class_='downloads')
        image_url = results.find("a")["href"]
        hemisphere_image_urls.append({'title':title, 'img_url':image_url})
    
    #Create Mars Summmary
    mars_summary = {}
    mars_summary["news_title"] = news_title
    mars_summary["news_p"] = news_p
    mars_summary["featured_image_url"] = featured_image_url
    mars_summary["mars_weather"] = mars_weather
    mars_summary["table_html"] = table_html
    mars_summary["hemisphere_image_urls"] = hemisphere_image_urls

    return mars_summary