# web-scraping-challenge

 Build a web application that scrapes various websites for data related to the Mission to Mars and display the information in a single HTML page.



 ## Scraping
 
 Create a Jupyter Notebook file called mission_to_mars.ipynb and use this to complete all of your scraping and analysis tasks. The following outlines what you need to scrape:


### NASA Mars News

Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.


### JPL Mars Space Images - Featured Image

Visit the url for JPL Featured Space Image and use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable.


### Mars Facts

Visit the Mars Facts and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc. Use Pandas to convert the data to a HTML table string.


### Mars Hemispheres

Visit the USGS Astrogeology site and save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data.



## MongoDB and Flask Application

Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.


 











