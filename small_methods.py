import os
from stemming.porter2 import stem

# omnipresent_words = ['www.', 'http:', 'https:', '.com', '.in']


def directory_manage(relative_location):  # checks if a directory exists or not if not then it creates it itself
	base_path = os.path.dirname(os.path.realpath(__file__))
	if not os.path.exists(os.path.join(base_path, relative_location)):
		os.makedirs(os.path.join(base_path, relative_location))

f = open('Processing_Data\\keywords.txt', 'r')
keywords = []
values = []
line_count = 0
for each_line in f:
	line_count += 1
	line = each_line.split()
	try:
		values.append(int(line[1]))
		keywords.append(stem(line[0]))
	except:
		directory_manage('Output\\Errors')
		f = open('Output\\Errors\\Keyword_Error.txt','a')
		f.write('Check Line No. '+str(line_count)+' in Output\\Errors\\keywords.txt for formatting error\n')
		f.close()
f.close()


def sort_links_wrt_importance(links, links_text):
	link_importance = []
	iterate = 0
	while iterate < len(links):
		link = stem(links[iterate])
		if isinstance(links_text[iterate], str):
			link_text = stem(links_text[iterate])
		else:
			link_text = 'ignore'
		# divided_link = link.split('/')
		i = 0
		strength = 0
		while i < len(keywords):
			if keywords[i] in link:
				strength += values[i]
			if isinstance(link_text, str):
				if keywords[i] in link_text:
					strength += values[i]
			i += 1
		link_importance.append(strength)
		iterate += 1
	i = 0
	while i < len(links):
		j = i
		# print('sorting')
		while j > 0:
			if link_importance[j] > link_importance[j-1]:
				temp_link = links[j]
				links[j] = links[j-1]
				links[j-1] = temp_link
				# temp_link_text = links_text[j]
				# links_text[j] = links_text[j-1]
				# links_text[j-1] = temp_link_text
				temp_imp = link_importance[j]
				link_importance[j] = link_importance[j-1]
				link_importance[j-1] = temp_imp
				j -= 1
			else:
				break
		i += 1
	return links
