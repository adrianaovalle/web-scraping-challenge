# Web Scraping Challenge
## Scraping
The following initial scraping was coded in file: mission_to_mars.py
### NASA Mars News
Latest news on Mars where scraped from: https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest

### Mars Space Images
Featured Mars image was scraped from: https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars

### Mars Weather
Mars weather was scraped from Twitter: https://twitter.com/marswxreport?lang=en


### Mars Facts
Mars facts were scraped from:  https://space-facts.com/mars/


### Mars Hemispheres
Mars pictures of the Hemispheres were scraped from: https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars

## MongoDB and Flak Application
### Scrape function
The file scrape_mars.py was created based on the code written in mission_to_mars.py.

### Call MongoDB and HTML
The file app.py does 2 things:
*Runs the scrape code and stores the results in MongoDB
*Finds the information in MongoDB and renders it in HTML

The final results is a Website that renders all the results.
