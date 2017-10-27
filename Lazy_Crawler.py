import small_methods
from bs4 import BeautifulSoup
from six.moves.urllib.request import urlopen
import Crawler_methods



base_url = input('Enter the url of website you want to crawl\n')
total_depth = int(input('Enter the depth upto which you want to crawl\n'))
set_of_all_links = {base_url}
live_queue = [base_url]
base_url = base_url.replace('www.', '')
base_url = base_url.replace('http://', '')
base_url = base_url.replace('https://', '')
# print(base_url)
temp_queue = []
depth = 0
while depth <= total_depth:
	for link in live_queue:
		Crawler_methods.get_links(link, temp_queue, set_of_all_links, base_url)
	live_queue = temp_queue
	print("Hello")
	print(temp_queue)
	print(live_queue)
	temp_queue.clear()
	depth+=1

print("all links were:-")
print(set_of_all_links)