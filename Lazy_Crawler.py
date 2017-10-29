import Crawler_methods
import small_methods

base_url = input('Enter the url of website you want to crawl\n')
total_depth = int(input('Enter the depth upto which you want to crawl\n'))
set_of_all_links = {base_url}
live_queue = [base_url]
base_url = base_url.replace('www.', '')
base_url = base_url.replace('http://', '')
base_url = base_url.replace('https://', '')

temp_queue = []
temp_queue_text = []
depth = 0
while depth <= total_depth:

	for link in live_queue:
		Crawler_methods.get_links(link, temp_queue, set_of_all_links, base_url, temp_queue_text)

	live_queue.clear()
	small_methods.directory_manage('output\\links')
	f = open('output\\links\Level ' + str(depth)+'.txt', 'w')
	temp_queue = small_methods.sort_links_wrt_importance(temp_queue, temp_queue_text)
	for link in temp_queue:
		f.write(str(link)+'\n')
		live_queue.append(link)
	# print(live_queue)
	# print(temp_queue_text)

	f.close()
	temp_queue_text.clear()
	temp_queue.clear()
	depth += 1

print("These are the links that we found :-")
print(set_of_all_links)
