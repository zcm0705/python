'''
@Author Jasmine Zhang
@Date June 14 2017
'''

from bs4 import BeautifulSoup
import requests
import json

def crawl():

	database = {}
	# the url for the first page is https://learn.adafruit.com/, need to fix later
	page_prefix = 'https://learn.adafruit.com/guides?guide_page='
	page = 1
	max_pages = 5
	while page <= max_pages:
		page_url = page_prefix + str(page)
		page_soup = cook_soup(page_url)
		for guide_block in page_soup.findAll('div', class_ = 'guide-block'):
			# convert from unicode to str type
			title_name = (guide_block.find(class_ = 'title').a.get_text().strip()).encode('utf-8')
			database[title_name] = {}

			# crawl brief info
			database[title_name]['Guide Info'] = crawl_guide_block(guide_block, title_name)
			
			# crawl item page
			item_url = get_item_url(guide_block)
			print title_name
			database[title_name]['Page Info'] = crawl_item_page(item_url)
			convert2json(database[title_name])
		page += 1

def crawl_guide_block(soup, title):
	guide = {'Title': title, 
		'Tagline': soup.find(class_ = 'tagline').a.get_text().strip(), 
		'Author': soup.find(class_ = "author").a.get_text().strip(), 
		# 'Img': soup.a.img.get('src'),  fix it later
		# 'Link': soup.find(class_ = 'title').a.get('href').strip(),
		'Link': get_item_url(soup).strip(),
		'Description': soup.find(class_ = "description").get_text().strip()}
	return guide

def get_item_url(soup):
	return 'https://learn.adafruit.com' + soup.find(class_ = 'title').a.get('href').strip()

def cook_soup(url):
	plain_text = requests.get(url).text
	soup = BeautifulSoup(plain_text, "html.parser")
	return soup

def convert2json(database):
	json_object = json.dumps(database, sort_keys=True, indent=4)
	print json_object

def crawl_item_page(url):
	# prepare soup
	soup = cook_soup(url)
	
	# use Dict structore to store data
	page_info = {}

	# divide the web page into three parts and crawl them seperately
	crawl_sidebar(soup.find("div", class_ = "sidebar-left-content"), page_info)
	# To be implemented
	# crawl_article(soup.find("article"), page_info)
	crawl_related_guides(soup.find(class_ = "related-guides-content row"), page_info)

	return page_info

def crawl_sidebar(soup, page_info):
	part = "Left Sidebar"
	page_info[part] = {}
	page_info[part]['Title'] = soup.find("div", class_ = "title").a.get_text()
	page_info[part]['Subtitle'] = soup.find("span", class_ = "tagline").a.get_text()
	
	page_info[part]['Topics'] = []
	for topic in soup.findAll("a", class_ = "sidebar-parent"):
		page_info[part]['Topics'].append(topic.get_text())

def crawl_related_guides(soup, page_info):
	part = "Related Guides"
	page_info[part] = []
	if soup is None:
		return
	for guide_block in soup.findAll(class_ = "guide-block"):
		page_info[part].append(guide_block.find(class_ = "title").a.get_text().strip())

# To be finished
# def crawl_article(soup, page_info):
# 	part = "Main Content"
# 	page_info[part] = {}
# 	page_info[part]["Article Title"] = soup.find("h1", class_ = "headline").span.get_text()
# 	page_info[part]["Arthor"] = soup.find("div", class_ = "author").a.get_text().strip()

# 	page_info[part]["Image"] = soup.find(class_ = "build-image").a.img.get('src');

# 	# get the word content
# 	word_content = soup.find(class_ = "markdown-html");
# 	page_info[part]["Word Content"] = {};
# 	# get the three paragraphs with the corresponding names
# 	p_names = [];
# 	for p_name in word_content.findAll("h2"):
# 		p_names.append(p_name.get_text().strip())

# 	paragraphs = []
# 	for paragraph in word_content.findAll("p"):
# 		paragraphs.append(paragraph.get_text().strip())

# 	for n in p_names:
# 		for p in paragraphs:
# 			page_info[part]["Word Content"][n] = p;

crawl()

