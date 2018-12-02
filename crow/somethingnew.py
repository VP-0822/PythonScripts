import requests
try:
	from bs4 import BeautifulSoup
except ImportError:
	import pip
	pip.main(['install', 'beautifulsoup4'])
	from bs4 import BeautifulSoup
import urllib.request
import sys

def getHTMLcontent(url):
	url = urllib.request.urlopen(url)
	htmldata = BeautifulSoup(url, 'html.parser')
	return htmldata

def getelementbyid(htmldata, elementid):
	if type(htmldata) == BeautifulSoup:
		element = htmldata.find(id=elementid)
		return element
	else:
		print('Invalid html data for parsing')
		return None

def getelementsbyclass(htmldata, elementclass):
	if type(htmldata) == BeautifulSoup:
		elements = htmldata.find_all('div', {'class': elementclass})
		return elements
	else:
		print('Invalid html data for parsing')
		return None



if __name__ == "__main__":
	print('Welcome! Happy Trading!!')
	user_input = 0
	while user_input is not -1 :
		scrip_name = input('Enter scrip name to fetch news or exit : ')
		scrip_name = scrip_name.upper()

		if scrip_name == 'EXIT':
			user_input = -1
			continue

		scripDict = {}
		scripDict['AL'] = 'https://www.moneycontrol.com/company-article/ashokleyland/news/AL'

		try:
			if scripDict[scrip_name] is None:
				print('Please ensure that you have added ' + scrip_name + ' to your portfolio.')
				continue
		except KeyError:
			print('Please ensure that you have added ' + scrip_name + ' to your portfolio.')
			continue

		scripURL = scripDict[scrip_name]
		NSE_NEWS_DIV_CLASS = 'MT15 PT10 PB10'
		MC_HOME = 'https://www.moneycontrol.com'
		scripData = getHTMLcontent(scripURL)
		elements = getelementsbyclass(scripData, NSE_NEWS_DIV_CLASS)
		allNewLinks = []
		for elm in elements:
			anchortag = elm.find('a')
			if anchortag is not None:
				allNewLinks.append(MC_HOME + anchortag['href'])
		for linkUrl in allNewLinks:
			linkData = getHTMLcontent(linkUrl)
			subLinks = linkData.find_all('a', class_='arial11_summ')
			if subLinks is not None:
				for anotherlink in subLinks:
					sp = BeautifulSoup(str(anotherlink),'html.parser')
					#tag = sp.a
					print(anotherlink)
        #for element in elements:
        #    print('news html '+ element.text)
