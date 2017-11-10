from bs4 import BeautifulSoup
from six.moves.urllib.request import urlopen
import small_methods
import re
import copy

extensions = ['.docx', '.pdf', '.mp4', '.mp3', '.jpg', '.jpeg', '.png', '.xlsx', '.xls', '.JPG', '.doc']


def fetch_url(url):   # fetches the url
	try:
		html = urlopen(url)
		return html

	except:
		small_methods.directory_manage("output\Errors")

		print(str(url) + " could not be opened")
		f = open('output/Errors/Link_Error.txt', 'a')
		f.write(str(url)+'\n')
		f.close()
		return int(1)


def extract_text(link):  # gets the text of the page
	link_data = fetch_url(link)
	html = link_data.read()
	soup = BeautifulSoup(html)

	for script in soup(["script", "style"]):
		script.extract()
	text = soup.get_text()
	lines = (line.strip() for line in text.splitlines())
	# break multi-headlines into a line each
	chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
	# drop blank lines
	text = '\n'.join(chunk for chunk in chunks if chunk)
	link1 = link
	link1 = re.sub('[^0-9a-zA-Z]+', '', link1)
	small_methods.directory_manage('output\\Websites_Text')
	f = open('output\\Websites_Text\link-' + str(link1) + '.txt', 'w')
	try:
		f.write(str(text))
	except:
		f.write(str(text.encode(encoding='UTF-8')))
	f.close()


def link_filter(link, temp_queue, all_links, base_url, temp_queue_text, link_text, home_url):
	link1 = str(link)

	for ext in extensions:
		if ext in link1:
			return  # does not add link if it is has any extension present in extensions

	if "#" in link1 or "mailto:" in link1:
		return
	if "www." not in link1 and "http" not in link1:
		link1 = base_url + link1

	if link1 in all_links:
		return 0
	home_url1 = copy.deepcopy(home_url)
	home_url1 = home_url1.replace('www.', '')
	home_url1 = home_url1.replace('http://', '')
	home_url1 = home_url1.replace('https://', '')
	if 'www.'+home_url1 not in link1 and 'http://'+home_url1 not in link1 and 'https://'+home_url1 not in link1:
		return 0
	temp_queue.append(link1)
	temp_queue_text.append(link_text)
	all_links.add(link1)
	return 1


def get_links(url, temp_queue, set_of_all_links, base_url, temp_queue_text):  # finds all links in the page
	link_data = fetch_url(url)
	if isinstance(link_data, int):
		return

	soup = BeautifulSoup(link_data, 'html.parser')

	# links_in_page = [a.attrs.get('href') for a in soup.find_all('a')]
	links_in_page = soup.find_all('a')
	base_on_page = soup.find('base')
	try:
		base_on_page_url = base_on_page.get('href')
	except:
		base_on_page_url = base_url

	for a_tag in links_in_page:
		link = a_tag.get('href')
		link_text = a_tag.string
		link_filter(link, temp_queue, set_of_all_links, base_on_page_url, temp_queue_text, link_text, base_url)
	# try:
	extract_text(url)
	"""except:
		print("No text extracted from"+ url)"""
