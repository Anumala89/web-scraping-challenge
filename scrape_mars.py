import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests

def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()


#NASA Mars News
    news_url ="https://mars.nasa.gov/news/"
    browser.visit(news_url)

    html = browser.html
    soup = bs(html, "html.parser")

    results = soup.find(id='main_container')

    news_elements = results.find_all('div', class_ ='list_text')
    news_titles = []
    paragraphs = []
    for elements in news_elements:
        title = elements.find('div', class_ = 'content_title').text
        para = elements.find('div', class_ ='article_teaser_body').text
        #if None in (title, para):
            #continue
        news_titles.append(title)
        paragraphs.append(para)
        
    news_title = news_titles
    paragraph = paragraphs


#JPL Mars Space Images-Features Image    
    img_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(img_url)

    html1 = browser.html
    soup1 = bs(html1, 'html.parser')

    for element in soup1.select("article"):
        image=element['style'].split("url('")[1].split("')")[0]
        featured_image_url = "https://www.jpl.nasa.gov" +image
    

#Mars Facts
    fact_url = "https://space-facts.com/mars/"
    tables = pd.read_html(fact_url)

    table = tables[0]
    table.columns=['Description', 'Mars']
    table = table.set_index('Description')
    fact_table = table.to_html()
    #fact_table.replace('\n', '')

#Mars Hemispheres
    url_list=["https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced",
          "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced",
          "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced",
          "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"]

    hemisphere_image_urls = []

    for url in url_list:
    
        r = requests.get(url)
        s = bs(r.text, 'html.parser')

        hemisphere_image_urls_dict = {}

        title = s.title.text.split('|')[0]
        hemisphere_image_urls_dict['title'] = title

        img = s.find('img', class_= 'wide-image')
        src= img.get('src')
        hemisphere_image_urls_dict['img_url'] = "https://astrogeology.usgs.gov/" + src
        hemisphere_image_urls.append(hemisphere_image_urls_dict)

        
#store data in a dictionary
    scrape_mars = {
        'news_title': news_title[0],
        'paragraph' : paragraph[0],
        'featured_image_url': featured_image_url,
        'fact_table': fact_table,
        'hemisphere_image_urls': hemisphere_image_urls
    }

# Close the browser after scraping
    browser.quit()

    return scrape_mars

#print(scrape())