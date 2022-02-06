
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriver

# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')

slide_elem.find('div', class_='content_title')

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'

img_url
#Mars Facts

df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

df.to_html()

browser.quit()


# Deliverable 1

# D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# Hemispheres

# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path)

# 1. Use browser to visit the URL 
# url = 'https://marshemispheres.com/'
url ='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

browser.visit(url)
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
#Parse the resulting html with soup
html = browser.html
hemi_soup = soup(html, 'html.parser')
# find the links
hemi_links = hemi_soup.find_all('h3')
#hemi_links
# loop through each hemisphere link
for hemi in hemi_links:
    # Navigate and click the link of the hemisphere
    img_page = browser.find_by_text(hemi.text)
    img_page.click()
    html= browser.html
    img_soup = soup(html, 'html.parser')
    # Scrape the image link
    img_url = 'https://astrogeology.usgs.gov/' + str(img_soup.find('img', class_='wide-image')['src'])
    # Scrape the title
    title = img_soup.find('h2', class_='title').text
    # Define and append to the dictionary
    hemi_dict = {'img_url': img_url,'title': title}
    hemisphere_image_urls.append(hemi_dict)
    browser.back()
#print(hemisphere_image_urls)

# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

# 5. Quit the browser
browser.quit()

