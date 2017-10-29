import os
from stemming.porter2 import stem

omnipresent_words = ['www.', 'http:', 'https:', '.com', '.in']

def directory_manage(relative_location):  # checks if a directory exists or not if not then it creates it itself
	base_path = os.path.dirname(os.path.realpath(__file__))
	if not os.path.exists(os.path.join(base_path, relative_location)):
		os.makedirs(os.path.join(base_path, relative_location))


def sort_links_wrt_importance(links, links_text):
	f = open('Processing_Data\\keywords.txt', 'r')
	keywords = []
	values = []
	for each_line in f:
		line = each_line.split()
		keywords.append(stem(line[0]))
		values.append(int(line[1]))
	f.close()

	link_importance = []
	iterate = 0
	while(iterate<len(links)):
		link = stem(links[iterate])
		if isinstance(links_text[iterate], str):
			link_text = stem(links_text[iterate])
		else:
			link_text = 'ignore'
		# divided_link = link.split('/')
		strength = 0
		i = 0
		strength = 0
		while i<len(keywords):
			if keywords[i] in link:
				strength += values[i]
			if isinstance(link_text, str):
				if keywords[i] in link_text:
					strength += values[i]
			i += 1
		link_importance.append(strength)
		iterate += 1
	i = 0
	while i<len(links):
		j = i
		# print('sorting')
		while(j>0):
			if(link_importance[j]>link_importance[j-1]):
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
		i+=1
	return links
	"""for word in divided_link:
			# for omni in omnipresent_words:
			#	word.replace(omni, '')
			# word = stem(word)

			i = 0
			while(i<len(keywords)):
				if(word==keywords[i]):
					strength +=	values[i]
				i+=1
		print(type(link_text))
		if isinstance(link_text, str):

			divided_link_text = link_text.split(' ')
			print(divided_link_text)
			for word in divided_link_text:
				word = stem(word)

				i = 0
				while(i<len(keywords)):
					if(word == keywords[i]):
						strength += values[i]
					i+=1

		link_importance.append(strength)
		iterate += 1
	print(links)
	print(link_importance)


sort_links_wrt_importance(['http://pec.ac.in', 'http://pec/faculties/teachers', 'http://pec/faculties'], ['college', 'faculties and teachers', 'faculties'])"""
