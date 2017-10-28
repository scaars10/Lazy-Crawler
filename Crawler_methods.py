from bs4 import BeautifulSoup
from six.moves.urllib.request import urlopen
import small_methods
import re


def fetch_url(url):
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


def extract_text(link):
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
	#  f = open('output\level' + str(depth) + '.txt', 'w')
	try:
		f.write(str(text))
	except:
		f.write(str(text.encode(encoding='UTF-8')))
	f.close()


def link_filter(link, temp_queue, all_links, base_url, base_link, url):
	#  nonlocal link
	link1 = str(link)
	if '.pdf' in link1:
		return 0

	if "www." not in link1 and "http" not in link1:
		if base_link != 'empty':
			link1 = base_link + link1
		else:
			link1 = url + link1

	if link1 in all_links:
		return 0
	if 'www.'+base_url not in link1 and 'http://'+base_url not in link1 and 'https://'+base_url not in link1:
		print(base_url + " not present in "+link1)
		return 0
	temp_queue.append(link1)
	all_links.add(link1)
	return 1


def get_links(url, temp_queue, set_of_all_links, base_url):
	link_data = fetch_url(url)
	if link_data is int:
		return
	try:

		soup = BeautifulSoup(link_data, 'html.parser')
	except:
		return
	links_in_page = [a.attrs.get('href') for a in soup.find_all('a')]
	base_on_page = soup.find('base')
	try:
		base_on_page.get('href')
	except:
		base_on_page = 'empty'

	for link in links_in_page:
		link_filter(link, temp_queue, set_of_all_links, base_url, base_on_page, url)
	extract_text(url)
	# print(temp_queue)
