Before running the crawler(Lazy_Crawler.py), run these commands in the git terminal or the terminal of your preference:
	pip install requests
	pip install bs4
	pip install six
	pip install stemming

Keywords used for sorting links with respect to their importance are present in \Processing_Data\keywords.txt
First word of each line is the keyword and the second word is an integer which shows its importance.
All the links from each level are present in \Output\links and the text of each page is present in \Output\Websites_Text
The errors encoutered in opening a link will be written in \Output\Errors\link_error.txt
and the errors in the keyword files will be written in \Output\Errors\keyword_error.txt 