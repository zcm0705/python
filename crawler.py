from bs4 import BeautifulSoup
import requests
import json

def spider():	
	# prepare soup
	url = 'https://learn.adafruit.com/sensors-in-makecode/buttons'
	plain_text = requests.get(url).text
	soup = BeautifulSoup(plain_text, "html.parser")
	
	# use Dict structore to store data
	dict = {}

	# divide the web page into three parts and crawl them seperately
	crawl_sidebar(soup.find("div", class_ = "sidebar-left-content"), dict)
	crawl_article(soup.find("article"), dict)
	crawl_related_guides(soup.find(class_ = "related-guides-content row"), dict)

	# convert to json object with some indentation
	json_object = json.dumps(dict, sort_keys=True, indent=4)
	print json_object
		
def crawl_sidebar(soup, dict):
	part = "Left Sidebar"
	dict[part] = {}
	dict[part]['Title'] = soup.find("div", class_ = "title").a.get_text()
	dict[part]['Subtitle'] = soup.find("span", class_ = "tagline").a.get_text()
	
	dict[part]['Topics'] = []
	for topic in soup.findAll("a", class_ = "sidebar-parent"):
		dict[part]['Topics'].append(topic.get_text())

def crawl_article(soup, dict):
	part = "Main Content"
	dict[part] = {}
	dict[part]["Article Title"] = soup.find("h1", class_ = "headline").span.get_text()
	dict[part]["Arthor"] = soup.find("div", class_ = "author").a.get_text().strip()

	dict[part]["Image"] = soup.find(class_ = "build-image").a.img.get('src');

	# get the word content
	word_content = soup.find(class_ = "markdown-html");
	dict[part]["Word Content"] = {};
	# get the three paragraphs with the corresponding names
	p_names = [];
	for p_name in word_content.findAll("h2"):
		p_names.append(p_name.get_text().strip())

	paragraphs = []
	for paragraph in word_content.findAll("p"):
		paragraphs.append(paragraph.get_text().strip())

	for n in p_names:
		for p in paragraphs:
			dict[part]["Word Content"][n] = p;


def crawl_related_guides(soup, dict):
	part = "Related Guides"
	dict[part] = []
	for guide_block in soup.findAll(class_ = "guide-block"):
		block = {}
		block["Title"] = guide_block.find(class_ = "title").a.get_text().strip()
		block["Subtitle"] = guide_block.find(class_ = "tagline").a.get_text().strip()
		block["Author"] = guide_block.find(class_ = "author").a.get_text().strip()
		# block["Gif"] = guide_block.find("video").get('poster')
		block["Description"] = guide_block.find(class_ = "description").get_text().strip()
		dict[part].append(block)



spider()

